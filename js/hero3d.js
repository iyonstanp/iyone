// IYONEX — cinematic 3D hero: a rotating node network around a glowing
// intelligence core (fleet / sensor mesh). Loads only where a
// <div data-hero3d> exists. Fails silently and leaves the static
// readouts/corner marks visible if Three.js or WebGL can't load.
(function () {
  "use strict";
  if (typeof THREE === "undefined") return;
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function makeGlowTexture() {
    var size = 128;
    var c = document.createElement("canvas");
    c.width = c.height = size;
    var ctx = c.getContext("2d");
    var g = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
    g.addColorStop(0, "rgba(255,255,255,1)");
    g.addColorStop(0.35, "rgba(255,255,255,0.55)");
    g.addColorStop(1, "rgba(255,255,255,0)");
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, size, size);
    return new THREE.CanvasTexture(c);
  }

  document.querySelectorAll("[data-hero3d]").forEach(function (mount) {
    var width = mount.clientWidth || 480;
    var height = mount.clientHeight || 420;

    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(42, width / height, 0.1, 100);
    camera.position.set(0, 0, 7.4);

    var renderer;
    try {
      renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    } catch (e) {
      return;
    }
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 1.75));
    renderer.setSize(width, height);
    mount.insertBefore(renderer.domElement, mount.firstChild);

    var group = new THREE.Group();
    scene.add(group);

    // ---- fibonacci-sphere node positions ----
    var COUNT = 52;
    var positions = [];
    var golden = Math.PI * (3 - Math.sqrt(5));
    for (var i = 0; i < COUNT; i++) {
      var y = 1 - (i / (COUNT - 1)) * 2;
      var radiusAtY = Math.sqrt(1 - y * y);
      var theta = golden * i;
      var x = Math.cos(theta) * radiusAtY;
      var z = Math.sin(theta) * radiusAtY;
      positions.push(new THREE.Vector3(x, y, z).multiplyScalar(2.4));
    }

    // ---- glowing sprite-based nodes, colour-shifted light blue -> deep blue ----
    var blue = new THREE.Color(0x5b9df9);
    var deepBlue = new THREE.Color(0x12306b);
    var nodeGeo = new THREE.BufferGeometry();
    var nodeColors = [];
    var flat = [];
    positions.forEach(function (p, idx) {
      flat.push(p.x, p.y, p.z);
      var c = blue.clone().lerp(deepBlue, idx / COUNT);
      nodeColors.push(c.r, c.g, c.b);
    });
    nodeGeo.setAttribute("position", new THREE.Float32BufferAttribute(flat, 3));
    nodeGeo.setAttribute("color", new THREE.Float32BufferAttribute(nodeColors, 3));
    var glowTex = makeGlowTexture();
    var nodeMat = new THREE.PointsMaterial({
      size: 0.22,
      map: glowTex,
      vertexColors: true,
      transparent: true,
      opacity: 0.95,
      depthWrite: false,
      blending: THREE.AdditiveBlending,
      sizeAttenuation: true,
    });
    group.add(new THREE.Points(nodeGeo, nodeMat));

    // ---- thin connecting lines between nearby nodes ----
    var lineVerts = [];
    var THRESH = 1.05;
    for (var a = 0; a < positions.length; a++) {
      for (var b = a + 1; b < positions.length; b++) {
        if (positions[a].distanceTo(positions[b]) < THRESH) {
          lineVerts.push(positions[a].x, positions[a].y, positions[a].z);
          lineVerts.push(positions[b].x, positions[b].y, positions[b].z);
        }
      }
    }
    var lineGeo = new THREE.BufferGeometry();
    lineGeo.setAttribute("position", new THREE.Float32BufferAttribute(lineVerts, 3));
    var lineMat = new THREE.LineBasicMaterial({ color: 0x2563eb, transparent: true, opacity: 0.28 });
    var lines = new THREE.LineSegments(lineGeo, lineMat);
    group.add(lines);

    // ---- faint outer wireframe shell for depth ----
    var shellGeo = new THREE.IcosahedronGeometry(2.95, 1);
    var shellMat = new THREE.MeshBasicMaterial({ color: 0x2563eb, wireframe: true, transparent: true, opacity: 0.1 });
    group.add(new THREE.Mesh(shellGeo, shellMat));

    // ---- glowing intelligence core at the centre ----
    var coreGeo = new THREE.IcosahedronGeometry(0.34, 1);
    var coreMat = new THREE.MeshBasicMaterial({ color: 0x2563eb, wireframe: true, transparent: true, opacity: 0.9 });
    var core = new THREE.Mesh(coreGeo, coreMat);
    group.add(core);
    var coreGlow = new THREE.Sprite(new THREE.SpriteMaterial({
      map: glowTex, color: 0x5b9df9, transparent: true, opacity: 0.55,
      blending: THREE.AdditiveBlending, depthWrite: false,
    }));
    coreGlow.scale.set(1.6, 1.6, 1.6);
    group.add(coreGlow);

    // ---- thin orbiting ring for a product-launch feel ----
    var ringGeo = new THREE.TorusGeometry(1.55, 0.006, 8, 96);
    var ringMat = new THREE.MeshBasicMaterial({ color: 0x5b9df9, transparent: true, opacity: 0.35 });
    var ring = new THREE.Mesh(ringGeo, ringMat);
    ring.rotation.x = Math.PI / 2.3;
    group.add(ring);

    // ---- interaction: gentle parallax toward pointer ----
    var targetX = 0, targetY = 0;
    mount.addEventListener("pointermove", function (e) {
      var r = mount.getBoundingClientRect();
      targetX = ((e.clientX - r.left) / r.width - 0.5) * 0.6;
      targetY = ((e.clientY - r.top) / r.height - 0.5) * 0.6;
    });

    // ---- entrance: scale + fade in ----
    var INTRO = reduceMotion ? 0 : 1.3;
    group.scale.setScalar(reduceMotion ? 1 : 0.82);
    [nodeMat, lineMat, shellMat, coreMat, ringMat].forEach(function (m) { m._targetOpacity = m.opacity; if (!reduceMotion) m.opacity = 0; });
    if (coreGlow.material) { coreGlow.material._targetOpacity = coreGlow.material.opacity; if (!reduceMotion) coreGlow.material.opacity = 0; }

    var clock = new THREE.Clock();
    function easeOutCubic(x) { return 1 - Math.pow(1 - x, 3); }

    function animate() {
      requestAnimationFrame(animate);
      var t = clock.getElapsedTime();

      if (t < INTRO) {
        var p = easeOutCubic(t / INTRO);
        group.scale.setScalar(0.82 + 0.18 * p);
        [nodeMat, lineMat, shellMat, coreMat, ringMat, coreGlow.material].forEach(function (m) {
          if (m && m._targetOpacity !== undefined) m.opacity = m._targetOpacity * p;
        });
      }

      if (!reduceMotion) {
        group.rotation.y = t * 0.14 + targetX;
        group.rotation.x = Math.sin(t * 0.15) * 0.08 + targetY;
        ring.rotation.z = t * 0.2;
        core.rotation.y = t * 0.6;
        core.rotation.x = t * 0.4;
        var pulse = 0.85 + Math.sin(t * 1.6) * 0.15;
        coreGlow.scale.setScalar(1.6 * pulse);
        lineMat.opacity = (lineMat._targetOpacity || 0.28) * (0.8 + Math.sin(t * 1.1) * 0.2);
      }

      renderer.render(scene, camera);
    }
    animate();

    window.addEventListener("resize", function () {
      var w = mount.clientWidth, h = mount.clientHeight;
      if (!w || !h) return;
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    });
  });
})();
