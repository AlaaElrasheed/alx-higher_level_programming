#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print python list
 * @p: list to be printed
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
    int size, alloc, i;
    const char *type;
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var = (PyVarObject *)p;

    size = var->ob_size;
    alloc = list->allocated;
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", alloc);

    for (i = 0; i < size; i++)
    {
        type = list->ob_item[i]->ob_type->tp_name;
        printf("Element %d: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list->ob_item[i]);
    }
}

/**
 * print_python_bytes - prints bytes
 * @p: bytes to be printed
 *
 * Return: Void
 */

void print_python_bytes(PyObject *p)
{
    unsigned char i, size;
    PyBytesObject *bytes = (PyBytesObject *)p;

    printf("[.] bytes object info\n");
    if (strcmp(p->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }
    printf("  size: %zd\n", ((PyVarObject *)p)->ob_size);
    printf("  trying string: %s\n", bytes->ob_sval);

    size = ((PyVarObject *)p)->ob_size;
    if (size > 10)
        size = 10;
    else
	    size++;
    printf("  first %d bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", bytes->ob_sval[i]);
        if (i == (size - 1))
            printf("\n");
        else
            printf(" ");
    }
}
