#include <Python.h>
#include </usr/include/python3.9/pyconfig-64.h>
#include <stdio.h>

/**
  * print_python_list_info - dhhfd
  * @p: djfjdf
  */
void print_python_list_info(PyObject *p)
{
	int siz, alooc, i;
	pyObject *obj;

	size = PY_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n, size");
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_Type(obj)->tp_name);
	}
}
