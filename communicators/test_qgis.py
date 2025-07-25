from operation import Operation

if __name__ == "__main__":
    # 1. 实例化操作类
    op = Operation(test_machine_ip="192.168.5.129", test_machine_port=8888)

    op.click_element(element_path="Project Toolbar/New", role_name_list=["tool bar", "push button"])

    op.click_element(element_path="Web", role_name_list=["menu item"])

    op.click_element(element_path="Web/QuickMapServices", role_name_list=["menu item", "menu item"])

    op.click_element(element_path="Web/QuickMapServices/OSM", role_name_list=["menu item", "menu item", "menu item"])

    op.click_element(element_path="Web/QuickMapServices/OSM/OSM Standard", role_name_list=["menu item", "menu item", "menu item", "menu item"])

    op.drag_to_percentage("QGIS3", 0.6, 0.7, 0.5, 0.6)

    op.click_element(element_path="Map Navigation Toolbar/Zoom to Layer(s)", role_name_list=["tool bar", "push button"])