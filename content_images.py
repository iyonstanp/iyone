# Free-to-use (Unsplash license, no attribution required) photography used
# across the site as illustrative industry/context imagery — never presented
# as an actual Iyonex product photo. Swap any of these for real product or
# facility photography once available (see README).

def _u(photo_id, w=1000, q=70):
    return f"https://images.unsplash.com/{photo_id}?w={w}&q={q}&auto=format&fit=crop"

IMG_ROBOT_ARM_BLUE   = _u("photo-1716191299980-a6e8827ba10b")   # blue industrial robot arm in factory
IMG_ROBOT_ARM_WHITE  = _u("photo-1655393001768-d946c97d6fd1")   # white robotic arm, clean studio setting
IMG_AUTOMOTIVE       = _u("photo-1567789884554-0b844b597180")   # vehicle inside factory with robot machines
IMG_WAREHOUSE        = _u("photo-1701313056413-0915e1adf204")   # large warehouse room with shelving
IMG_MANUFACTURING    = _u("photo-1777383975764-bec6f5cabf00")   # robotic arms assembling a car chassis
IMG_HEAVY_INDUSTRY   = _u("photo-1701328778019-e95dedbf5346")   # factory filled with machines and boxes
IMG_ELECTRONICS      = _u("photo-1647427060118-4911c9821b82")   # factory floor with orange machines
IMG_WORKSHOP_STUDENT = _u("photo-1581092160607-ee22621dd758")   # student operating machinery in a workshop
IMG_TEAM_ENGINEERING = _u("photo-1581091226033-d5c48150dbaa")   # engineers reviewing work on a laptop
