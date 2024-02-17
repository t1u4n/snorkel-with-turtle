import pytest
from labeling_function_lib.labeling_function_lib import LabelingFunctionLib

def dummy_label_func(item):
    return "dummy_label"

def test_register_and_get():
    lib = LabelingFunctionLib()
    lib.register("dummy", dummy_label_func)
    assert lib.get("dummy") == dummy_label_func, "Failed to register or get the label function"

def test_register_existing_name():
    lib = LabelingFunctionLib()
    lib.register("dummy", dummy_label_func)
    with pytest.raises(ValueError):
        lib.register("dummy", dummy_label_func)

def test_register_not_callable():
    lib = LabelingFunctionLib()
    with pytest.raises(TypeError):
        lib.register("not_callable", "this is not a function")

def test_get_non_existent():
    lib = LabelingFunctionLib()
    with pytest.raises(LookupError):
        lib.get("non_existent")

def test_get_all():
    lib = LabelingFunctionLib()
    lib.register("dummy1", dummy_label_func)
    lib.register("dummy2", dummy_label_func)
    assert len(lib.get_all()) == 2, "Failed to retrieve all label functions"

def test_unregister():
    lib = LabelingFunctionLib()
    lib.register("dummy", dummy_label_func)
    lib.unregister("dummy")
    with pytest.raises(LookupError):
        lib.get("dummy")

def test_clear():
    lib = LabelingFunctionLib()
    lib.register("dummy1", dummy_label_func)
    lib.register("dummy2", dummy_label_func)
    lib.clear()
    assert len(lib.get_all()) == 0, "Failed to clear all label functions"
