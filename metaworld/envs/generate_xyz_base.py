from lxml import etree

tree = etree.parse("./assets_v2/objects/assets/xyz_base.xml")

root = tree.getroot()

leftpad_body = root.find(".//body[@name='rightpad']")

geom_x = 32
geom_z = 32

claw_x = 0.045
claw_y = 0.003
claw_z = 0.030

size_x = claw_x / geom_x
size_y = claw_y
size_z = claw_z / geom_z


# <geom name="leftpad_geom" condim="4" margin="0.001" type="box" user="0" pos="0 0 0" size="0.045 0.003 0.015" rgba="0 1 1 1.0" solimp="0.95 0.99 0.01" solref="0.01 1" friction="2 0.1 0.002" contype="1" conaffinity="1"/>

if leftpad_body is not None:
    # delete all geoms with class="base_col"
    for geom in leftpad_body.findall("geom"):
        # print(geom.get("name"))
        # leftpad_body.remove(geom)
        pass

    for i in range(-geom_x + 1, geom_x, 2):
        for j in range(-geom_z + 1, geom_z, 2):
            pos_x = i * size_x
            pos_y = 0
            pos_z = j * size_z

            geom = etree.SubElement(leftpad_body, "geom")
            geom.tail = "\n"
            geom.set("group", "4")
            geom.set("condim", "4")
            geom.set("margin", "0.001")
            geom.set("type", "box")
            geom.set("user", "0")
            geom.set("pos", f"{pos_x} {pos_y} {pos_z}")
            geom.set("size", f"{size_x} {size_y} {size_z}")
            geom.set("rgba", "0 1 1 1.0")
            geom.set("solimp", "0.95 0.99 0.01")
            geom.set("solref", "0.01 1")
            geom.set("friction", "2 0.1 0.002")
            geom.set("contype", "1")
            geom.set("conaffinity", "1")

    # add new geoms

tree.write(
    "./assets_v2/objects/assets/xyz_base.xml", pretty_print=True, encoding="utf-8"
)

# <geom class="base_col" name="leftclaw_it_l1" condim="4" margin="0.001" type="box" user="0" pos="0.039375 0 0.0075" size="0.005625 0.003 0.0075"  rgba="0 1 1 1.0"  />
