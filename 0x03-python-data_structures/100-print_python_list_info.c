#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p) {

  Py_ssize_t size = PyList_Size(p);

  PyListObject *list = (PyListObject*)p;
  
  printf("[*] Size of the Python List = %zd\n", size);
  printf("[*] Allocated = %zd\n", list->allocated);

  for (Py_ssize_t i = 0; i < size; i++) {
    PyObject *item = PyList_GetItem(p, i);
    printf("Element %zd: %s\n", i, item->ob_type->tp_name); 
  }

}
