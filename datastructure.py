/*Data structures: List, Stacks and Queues
Objectives:
Students at the end of the classes should be able to demonstrate mastery of:
 The concept of Abstract Data Types (ADTs).
 How to efficiently perform operations on lists.
 The stack ADT and its use in implementing recursion.
 The queue ADT and its use in operating systems and algorithm design.
Description
 List
 Array based List Implementation
 Linked Lists
 Comparison of List implementations
 Element implementation
 Doubly Linked Lists
 Stacks
 Array-Based Stacks
 Linked stacks
 Comparison of Array-Based and Linked Stacks
 Implementing Recursion
 Queues
 Array-Based Queues
 Linked Queues
 Comparison and Array-Based and Linked Queues
To manage the complexity of problems and the problem-solving process, we use abstractions to allow them 
to focus on the “big picture” without getting lost in the details. By creating models of the problem domain, 
we are able to utilize a better and more efficient problem-solving process. These models allow us to describe 
the data that our algorithms will manipulate in a much more consistent way with respect to the problem itself.
Abstract Data Type ADT 
An abstract data type, sometimes abbreviated ADT, is a mathematical model for data types; a logical 
description of how we view the data and the operations that are allowed without regard to how they will be 
implemented. This means that we are concerned only with what the data is representing and not with how it 
will eventually be constructed. By providing this level of abstraction, we are creating an encapsulation around 
the data. The idea is that by encapsulating the details of the implementation, we are hiding them from the 
user’s view. This is called information hiding.
ADT may be formally described as a 
"class of objects whose logical behaviour is defined by a set of values and a set of operations" (Dale & 
Walker, 1996)
For instance:
i. Integers are an ADT, defined as the values …, −2, −1, 0, 1, 2, …, and by arithmetic and logical 
operations such as addition, subtraction, multiplication, division, greater than, less than, etc., 
ii. An abstract stack, which is a last-in-first-out structure, could be defined by three operations: push, pop 
and peek or top.
iii. An abstract queue, which is a first-in-first-out structure, would also have three operations: enqueue, 
dequeue, and front.
In essence, an ADT consists of an abstract data structure and operations. 
The implementation of an abstract data type is referred to as a data structure. 
Data Structure
Data structure is the structural representation of logical relationships between elements of data. In other words, 
a data structure is a way of organizing data items by considering its relationship to each other.
Data structure mainly specifies the structured organization of data, by providing accessing methods with correct 
degree of associativity. It is a specialized way of collecting, organising and storing data in such a way that we 
can perform operations on these data efficiently. It involves rendering data elements in terms of some 
relationship, for better organization and storage. 
Data structure is a collection of data values, the relationships among them, and the functions or operations 
that can be applied to the data.
Different kinds of data structures are suited to different kinds of applications, and some are highly specialized 
to specific tasks. For example, relational databases commonly use B-tree indexes for data retrieval, while 
compiler implementations usually use hash tables to look up identifiers.
Data structure should be designed and implemented in such a way that it reduces the complexity and increases 
the efficiency. To achieve this, it will require that we provide a physical view of the data using some collection 
of programming constructs and primitive data types. 
Data structure can be viewed either as built in data structures which are as primitive data types such as Integer, 
Float, Boolean, Char etc. or as user defined data structures such as arrays, lists etc.
Basic Operations
The data in the data structures are processed by certain operations. The particular data structure chosen largely 
depends on the frequency of the operation that needs to be performed on the data structure.
 Traversing: Accessing each record exactly once so that certain items in the record may be processed.
 Searching: finding the location of the record with a given key value or finding the locations of all 
records which satisfy one or more conditions.
 Insertion: Adding a new record to the structure
 Deletion: Removing a record from the structure
 Sorting: Arranging the records in some logical order
 Merging: Combining the records in two different sorted files into a single sorted file.
The two major categories of Data Structures are Static Structures Dynamic Structures. Each has its own set of 
advantages and disadvantages.
Static Data Structures 
Static data structures are designed to store static “set of data”. However, static “set of data”, doesn’t mean that 
we cannot change the assigned values of elements. It is the memory size allocated to “data”, which is static. 
So that, it is possible to change content of a static structure but without increasing the memory space allocated 
to it.
 
Dynamic Data Structures 
Dynamic data structures are designed to facilitate change of data structures in the runtime. It is possible to 
change the assigned values of elements, as it was with static structures. Also, in dynamic structures the initially 
allocated memory size is not a problem. It is possible to add new elements, remove existing elements or do 
any kind of operation on data set without considering about the memory space allocated initially.
 
 
Static Data Structures vs. Dynamic Data Structures 
Static data structure is given a fixed area of memory which it can operate within. It is not possible to expand 
this fixed size in the run time. Consequently, location of each element is fixed and known by the program. 
Dynamic data structure also has an area where it can operate. However, this size of the area is flexible, not 
fixed as it was with static data structures. It is possible to expand or contract the area as required, by adding 
or removing elements from data structure.
We look at the differences in the following ways:
 Access to elements: Static data structure has a fixed size. Also, elements of static data structures have 
fixed locations. But in dynamic structures, elements are added dynamically. So that, the locations of 
elements are dynamic and determined at runtime. A program will have to refer a common object or, 
go through the structure to find required element. E.g. Consider that values denoted as “AXX” are 
memory address. Consider that we need to access element “D”. In the static structure, it is possible to 
directly access the memory location “A04” as it is already known by the program. However, in dynamic 
structure, elements are added to the data structure dynamically. Sometimes even by different 
components of a program. Consider the scenario of linked lists. When we need to access element “D”, 
program doesn’t know that it is located in “A65” memory location. 
So, program starts with the initial element which is “A” located in “A01”. Element A points to the next 
element, which is B. B points to C and C in turn points to D. In order to access a single element, it was 
required to go through the linked list. However, it is possible to create a common object which keep 
track of memory location of each object and use it to directly access an element of a dynamic structure. 
Even in that case, it is a must to access number of objects to do so. It is clear that access to elements of 
data structures is efficient with static structures, than it is with dynamic structures.
 Insertions and Removals: As discussed earlier, static structure has fixed sizes. It is possible to remove the 
value of an element, but the element is still there in the structure. Only difference is that element 
doesn’t contain any data. Such removal is not going to free the memory occupied by the element and 
can be considered as a waste of resources. What about adding new elements to a static structure? As 
we already know it is not possible because static data structure has a fixed size. In order to add new 
element, we should create a new static structure with number of elements required and move the data 
from existing structure to new structure and assign additional elements with required values. Unlike 
static data structures, dynamic data structures are flexible. They do not have a fixed number of element 
or fixed size. So it is possible to add or remove elements easily. Consider a linked list as an example. 
As discussed earlier, elements of a linked list points to next element of the list. Imagine that you want 
to remove element “C” of a linked list. “B” is pointing at “C” and “C” is pointing at element “D”. If 
we remove element “C”, element “B” should point to element “D”, to keep the linked list unbroken. 
So what we have to do is just changing the pointers and assign element “C” with a NULL value, so that 
garbage collator (or similar mechanism) will remove the object and release the memory consumed by 
that object. Addition of new items to a dynamic data structure is also similar to the process of removal. 
Imagine that we want to add an element after element “B” and before element “C”. What we have to 
do is simply adding the new element to memory, changing pointer of B to point to newly added 
element and setting pointer of new element to point at element “C”.
 
 
So it is clear that, removal of an element from Static Data Structure is not possible. It is possible to 
remove or null the value of element, but it will not free the memory consumed by the element. It is 
possible to create a new static data structure and move the data from previous structure, excluding the 
valued needed to be removed. However, it is a resource consuming process, as it creates number of 
instances of data structures to complete the process. When it comes to dynamic data structures, removal 
is efficient and easy to manage. In linked lists, it is all about setting an object to null and changing some 
pointers. No new objects will be created and resource consume is at minimum. Insertion is also same, 
static structures have a fixed size, so insertion of elements in not possible. The only way of inserting 
elements to a static data structure is creating a new data structure with required number of elements 
and copying the previous values in to new structure. This is again a resource consuming process. Think 
of a array containing 1000 elements and you want to add a new element at the end. You’ll have to 
create a new array with 1001 elements and move values from previous array to new array making 
number of calls. But when it comes to dynamic structure, addition of an element is a simple process. 
In linked lists, it is just creation of an object and changing two pointers. When compared with static 
data structures, resource consume is at minimum and resources are used effectively.
 
Advantages and Disadvantages 
According to above discussion it is clear that dynamic data structures have the following attributes:
 Ability to efficiently add, remove or modify elements
 Flexible size
 Effective use of resources – because resources are allocated at the runtime, as required.
 Slower access to elements (when compared with static data structures)
Static data structures have the following characteristics:
 Faster access to elements (when compared with dynamic data structures)
 Add, remove or modify elements is not directly possible. If done, it is a resource consuming process.
 Fixed size.
 Resources allocated at creation of data structure, even if elements do not contain any value.
So, it is clear that both data structures have advantages and disadvantages. It is not effective to use dynamic 
structures to store set of data that is known, not to change. Using static data structure in such case will save 
system resources and also provide faster access to elements. Users or developers should adapt the suitable data 
structures based on situation.
 
Data structures can also be classified as either linear or non-linear based on arrangement of data. 
 
Linear Data Structures 
Data structure can be referred to as linear if its elements form a sequence or a linear list. Data arrangement is 
linear, although storage does not necessarily have to be sequential. 
Stacks, queues, deques, and lists are examples of data collections whose items are ordered depending on how 
they are added or removed. Once an item is added, it stays in that position relative to the other elements that 
came before and came after it. Collections such as these are often referred to as linear data structures.
Linear structures can be thought of as having two ends. Sometimes these ends are referred to as the “left” and 
the “right” or in some cases the “front” and the “rear.” You could also call them the “top” and the “bottom.” 
The names given to the ends are not significant. What distinguishes one linear structure from another is the 
way in which items are added and removed, in particular the location where these additions and removals 
occur. For example, a structure might allow new items to be added at only one end. Some structures might 
allow items to be removed from either end. These variations give rise to some of the most useful data structures 
in computer science. They appear in many algorithms and can be used to solve a variety of important 
problems.
List 
A list is a finite, ordered sequence of data items known as elements.
By “ordered”, we do not mean sorted, rather we mean that each element has a position in the list. There 
might or might not be some relationship between the value of an element and its position in the list. E.g., 
sorted lists have their elements positioned in ascending order of value, while unsorted lists have no particular 
relationship between element values and positions.
A list is of the form 𝑎𝑎1, 𝑎𝑎2, 𝑎𝑎3, … , 𝑎𝑎𝑛𝑛
We say that the size of this list is n. A special list of size 0 is referred to as a null list.
For any list except the null list, we say that 𝑎𝑎𝑖𝑖+1 succeeds) 𝑎𝑎𝑖𝑖 (i < n) and that 𝑎𝑎𝑖𝑖−1 precedes 𝑎𝑎𝑖𝑖 (i > 1). 
The first element of the list is 𝑎𝑎1, and the last element is 𝑎𝑎𝑛𝑛. 
The position of element 𝑎𝑎𝑖𝑖 in a list is 𝑖𝑖. 
Elements in a list can be just integers or arbitrarily complex elements. In simple list implementations, all 
elements of the list have the same data type, although there is no conceptual objection to lists whose elements 
have differing data types if the application requires it. 
The operations defined as part of the list ADT do not depend on the elemental data type. For example, the 
list ADT can be used for lists of integers, lists of characters, lists of payroll records, even lists of lists.
A list is said to be empty when it contains no elements. The number of elements currently stored in the list is 
called the length of the list. The beginning of the list is called the head, while the end of the list is called the 
tail. 
Some operations that can be performed on list include print_list, make_null; 
find, returns the position of the first occurrence of a key; 
insert and delete, insert and delete some key from some position in the list; and 
find_kth, returns the element in some position (specified as an argument). 
e.g. Given the following list: 34, 12, 52, 16, 12, 
find(52) will return 3; 
insert(x,3) might make the list into 34, 12, 52, x, 16, 12 (if we insert after the position given); and 
delete(3) might turn that list into 34, 12, x, 16, 12.
Ultimately, the interpretation of what is appropriate for a function is entirely up to the programmer.
Additional operations may include next and previous, which would take a position as argument and return 
the position of the successor and predecessor, respectively.
There are two standard approaches to implementing lists, the array-based list, and the linked list.
Array Implementation of Lists 
List can be implemented just by using an array. 
An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of 
the same type together. This makes it easier to calculate the position of each element by simply adding an 
offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the 
name of the array).
Each element of an array can be uniquely identified by their index in the array
If the array is dynamically allocated, an estimate of the maximum size of the list is required. Usually this requires 
a high over-estimate, which wastes considerable space. This could be a serious limitation, especially if there are 
many lists of unknown sizes.
An array implementation allows print_list and find to be carried out in linear time, which is as good as can be 
expected, and the find_kth operation takes constant time. However, insertion and deletion are expensive. For 
example, inserting at position 0 (which amounts to making a new first element) requires first pushing the entire 
array down one spot to make room, whereas deleting the first element requires shifting all the elements in the 
list up one, so the worst case of these operations is O(n). On average, half the list needs to be moved for either 
operation, so linear time is still required. Merely building a list by 𝑛𝑛 successive inserts would require quadratic 
time.
Because the running time for insertions and deletions is so slow and the list size must be known in advance, 
simple arrays are generally not used to implement lists.
#include<stdio.h>
#include<conio.h>
#define MAX 10
void create();
void insert();
void deletion();
void search();
void display();
int a, b[20], n, p, e, f, i, pos;
void main()
{
//clrscr();
int ch;
char g='y';
do
{
printf("\n main Menu");
printf("\n 1.Create \n 2.Delete \n 3.Search \n 4.Insert \n 5.Display\n 6.Exit \n");
printf("\n Enter your Choice");
scanf("%d", &ch);
switch(ch)
{
case 1:
create();
break;
case 2:
deletion();
break;
case 3:
search();
break;
case 4:
insert();
break;
case 5:
display();
break;
case 6:
exit();
break;
default:
printf("\n Enter the correct choice:");
}
printf("\n Do u want to continue:::");
scanf("\n%c", &g);
}
while(g=='y'||g=='Y');
getch();
}
void create()
{
printf("\n Enter the number of nodes");
scanf("%d", &n);
for(i=0;i<n;i++)
{
printf("\n Enter the Element:",i+1);
scanf("%d", &b[i]);
}
}
void deletion()
{
printf("\n Enter the position you want to delete::");
scanf("%d", &pos);
if(pos>=n)
{
printf("\n Invalid Location::");
}
else
{
for(i=pos+1;i<n;i++)
{
b[i-1]=b[i];
}
n--;
}
printf("\n The Elements after deletion");
for(i=0;i<n;i++)
{
printf("\t%d", b[i]);
}
}
void search()
{
printf("\n Enter the Element to be searched:");
scanf("%d", &e);
for(i=0;i<n;i++)
{
if(b[i]==e)
{
printf("Value is in the %d Position", i);
}
else
{
printf("Value %d is not in the list::", e);
continue;
}
}
}
void insert()
{
printf("\n Enter the position u need to insert::");
scanf("%d", &pos);
if(pos>=n)
{
printf("\n invalid Location::");
}
else
{
for(i=MAX-1;i>=pos-1;i--)
{
b[i+1]=b[i];
}
printf("\n Enter the element to insert::\n");
scanf("%d",&p);
b[pos]=p;
n++;
}
printf("\n The list after insertion::\n");
display();
}
void display()
{
printf("\n The Elements of The list ADT are:");
for(i=0;i<n;i++)
{
printf("\n\n%d", b[i]);
}
}
Linked list 
The linked list is used to circumvent the problems and linear cost of insertion and deletion in the array based 
implementation of list. It helps us to avoid contiguous storage of the elements in the list. 
A linked list is a set of dynamically allocated nodes, arranged in such a way that each node contains one value 
and one pointer. The elements of the list are not stored at contiguous memory locations but are linked using 
pointers. The pointer always points to the next member of the list. 
A linked list is held using a local pointer variable which points to the first item of the list. 
The linked list consists of a series of structures, which are not necessarily adjacent in memory. Each structure 
contains the element and a pointer to a structure containing its successor. We call this the next pointer. The 
next field of the last pointer is set to NULL. In addition to the cells of the list, we need a pointer variable, call 
it top which points to the first item in the list. If the list is empty, we set the value of top to NULL. 
There are 3 different implementations of Linked List available, they are:
 Singly Linked List
 Doubly Linked List
 Circular Linked List
In a Singly Linked List, each node contains a pointer which points to the next node in the list. We can think of 
each node as a cell with two fields. 
Data Next
Data can actually be one or more fields.
The graphical depiction of linked list is below:
Recall that a pointer variable is just a variable that contains the address where some other data is stored. Thus, 
if 𝑝𝑝 is declared to be a pointer to a structure, then the value stored in 𝑝𝑝 is interpreted as the location, in main 
memory, where a structure can be found. 
A field of that structure can be accessed by 𝑝𝑝 field_name, where field_name is the name of the field we wish 
to examine. 
In the figure below, the list contains five structures, which happen to reside in memory locations 1000, 800, 
712, 992, and 692 respectively. The next pointer in the first structure has the value 800, which provides the 
indication of where the second structure is. The other structures each have a pointer that serves a similar 
purpose. Of course, in order to access this list, we need to know where the first cell can be found. A pointer 
variable can be used for this purpose. It is important to remember that a pointer is just a number. 
Deletion operation in a linked list
 
Insertion operation in a linked list
 
Advantages of Linked Lists
 Linked list structure is dynamic i.e. there is no need to define initial size; memory allocation is done 
when required
 Insertion and deletion operations can be easily implemented even from the middle of the list.
 It makes the implementation of Stacks and queues easier.
 Linked List reduces the access time.
Disadvantages of Linked Lists
 Elements cannot be accessed randomly; it has to access each node sequentially - it is impossible to reach 
the nth item in the array without first iterating over all items up until that item. This means we have 
to start from the beginning of the list and count how many times we advance in the list until we get 
to the desired item.
 Dynamic memory allocation and pointers are required, which complicates the code and increases the 
risk of memory leaks and segment faults.
 Linked lists have a much larger overhead over arrays, since linked list items are dynamically allocated 
(which is less efficient in memory usage) and each item in the list also must store an additional pointer.
 The memory is wasted as pointers require extra memory for storage.
Applications of Linked Lists
 Linked lists are used to implement stacks, queues, graphs, etc.
 Linked lists let you insert elements at the beginning and end of the list.
 In Linked Lists we don't need to know the size in advance.
Implementation in C 
Since each node consists of at least two fields, we use a struct to define the format of the node. The next
field is a pointer to a structure which it is a part of. Thus, the definition of the structure includes a field which
points to the structure being defined; this is called self-referencing structure. 
Suppose the data at each node is a positive integer, we can define a node as follow:
struct node {
 int val;
 struct node * next;
};
Or using typedef:
#include <stdio.h>
int main() {
 typedef struct node {
 int val;
 struct node * next;
 } node_t;
 
return 0;
}
Note that we name our node type node_t so we can use the nodes.
The variable top can now be defined as a pointer to a node thus:
Node *top;
Or
NodePtr top;
In contrast to array’s static method of specifying size beforehand, for linked list storage is allocated for the 
node and pointers set appropriately only whenever a new node must be added to the list; thus we allocate 
just the right amount of storage for the list – no more, no less. Allocating storage as needed is referred to as 
dynamic storage allocation. In C, we allocate storage dynamically by using the standard functions malloc and 
calloc. In order to use these functions and free later, the program must be preceeded by the header line
#include <stdlib.h>
The prototype for malloc is
void *malloc(size_t size);
size_t is an implementation-defined unsigned integer type defined in the standard header <stddef.h>. 
typically, size_t is typedef ‘d as unsigned int or unsigned long int.
To create a local variable which points to the first item of the list (called head).
#include <stdio.h>
int main() {
 node_t * head = NULL;
 head = malloc(sizeof(node_t));
 if (head == NULL) {
 return 1;
 }
 
 head->val = 1;
 head->next = NULL;
 
return 0
We have created the first variable in the list. We must set the value, and the next item to be empty, if we want 
to finish populating the list. Our program should always check if malloc returned a NULL value or not.
To add a variable to the end of the list, we can just advance to the next pointer:
#include <stdio.h>
int main() {
 node_t * head = NULL;
 head = malloc(sizeof(node_t));
 head->val = 1;
 head->next = malloc(sizeof(node_t));
 head->next->val = 2;
 head->next->next = NULL;
 
return 0;
}
This can go on and on, but what we should actually do is advance to the last item of the list, until the next 
variable will be NULL.
Iterating over a list 
Let's build a function that prints out all the items of a list. To do this, we need to use a current pointer that 
will keep track of the node we are currently printing. After printing the value of the node, we set the current 
pointer to the next node, and print again, until we've reached the end of the list (the next node is NULL).
#include <stdio.h>
int main() {
 void print_list(node_t * head) {
 node_t * current = head;
 
 while (current != NULL) {
 printf("%d\n", current->val);
 current = current->next;
 }
 }
return 0;
Adding an item to the end of the list 
To iterate over all the members of the linked list, we use a pointer called current. We set it to start from the 
head and then in each step, we advance the pointer to the next item in the list, until we reach the last item.
#include <stdio.h>
int main() {
 void push(node_t * head, int val) {
 node_t * current = head;
 while (current->next != NULL) {
 current = current->next;
 }
 
 /* now we can add a new variable 
 current->next = malloc(sizeof(node_t));
 current->next->val = val;
 current->next->next = NULL;
 }
 
return 0;
}
The best use cases for linked lists are stacks and queues, which we will now implement:
Adding an item to the beginning of the list (pushing to the list) 
To add to the beginning of the list, we will need to do the following:
 Create a new item and set its value
 Link the new item to point to the head of the list
 Set the head of the list to be our new item
This will effectively create a new head to the list with a new value, and keep the rest of the list linked to it.
Since we use a function to do this operation, we want to be able to modify the head variable. To do this, we 
must pass a pointer to the pointer variable (a double pointer) so we will be able to modify the pointer itself.
#include <stdio.h>
int main() {
 void push(node_t ** head, int val) {
 node_t * new_node;
 new_node = malloc(sizeof(node_t));
 
 new_node->val = val;
 new_node->next = *head;
 *head = new_node;
 }
 
return 0;
}
Removing the first item (popping from the list) 
To pop a variable, we will need to reverse this action:
 Take the next item that the head points to and save it
 Free the head item
 Set the head to be the next item that we've stored on the side
Here is the code:
#include <stdio.h>
int main() {
 int pop(node_t ** head) {
 int retval = -1;
 node_t * next_node = NULL;
 
 if (*head == NULL) {
 return -1;
 }
 
 next_node = (*head)->next;
 retval = (*head)->val;
 free(*head);
 *head = next_node;
 
 return retval;
 }
 
return 0;
}
Removing the last item of the list 
Removing the last item from a list is very similar to adding it to the end of the list, but with one big exception 
- since we have to change one item before the last item, we actually have to look two items ahead and see if 
the next item is the last one in the list:
#include <stdio.h>
int main() {
 int remove_last(node_t * head) {
 int retval = 0;
 /* if there is only one item in the list, remove it 
 if (head->next == NULL) {
 retval = head->val;
 free(head);
 return retval;
 }
 
 /* get to the second to last node in the list 
 node_t * current = head;
 while (current->next->next != NULL) {
 current = current->next;
 }
 
 /* now current points to the second to last item of the list, so let's remove current->next 
 retval = current->next->val;
 free(current->next);
 current->next = NULL;
 return retval;
 
 }
 
return 0;
}
Removing a specific item 
To remove a specific item from the list, either by its index from the beginning of the list or by its value, we 
will need to go over all the items, continuously looking ahead to find out if we've reached the node before 
the item we wish to remove. This is because we need to change the location to where the previous node 
points to as well.
Here is the algorithm:
 Iterate to the node before the node we wish to delete
 Save the node we wish to delete in a temporary pointer
 Set the previous node's next pointer to point to the node after the node we wish to delete
 Delete the node using the temporary pointer
There are a few edge cases we need to take care of, so make sure you understand the code.
#include <stdio.h>
int main() {
 int remove_by_index(node_t ** head, int n) {
 int i = 0;
 int retval = -1;
 node_t * current = *head;
 node_t * temp_node = NULL;
 
 if (n == 0) {
 return pop(head);
 }
 
 for (i = 0; i < n-1; i++) {
 if (current->next == NULL) {
 return -1;
 }
 current = current->next;
 }
 
 temp_node = current->next;
 retval = temp_node->val;
 current->next = temp_node->next;
 free(temp_node);
 
 return retval;
 
 }
 
return 0;
}
Stack 
 
A stack (sometimes called a “push-down stack”) is a basic data structure that can be logically thought as linear 
structure represented by a real physical stack or pile. It is an ordered collection of items where the addition of 
new items and the removal of existing items always takes place at the same end. This end is commonly referred 
to as the “top.” The end opposite the top is known as the “base.” The base of the stack is significant since items 
stored in the stack that are closer to the base represent those that have been in the stack the longest. The most 
recently added item is the one that is in position to be removed first. This ordering principle is sometimes 
called LIFO, last-in first-out. It provides an ordering based on length of time in the collection. Newer items are 
near the top, while older items are near the base.
Many examples of stacks occur in everyday situations. Almost any cafeteria has a stack of trays or plates where 
you take the one at the top, uncovering a new tray or plate for the next customer in line. The only book 
whose cover is visible is the one on top. To access others in the stack, we need to remove the ones that are 
sitting on top of them. Also, every web browser has a Back button. As you navigate from web page to web 
page, those pages are placed on a stack (actually it is the URLs that are going on the stack). The current page 
that you are viewing is on the top and the first page you looked at is at the base. If you click on the Back 
button, you begin to move in reverse order through the pages.
There are basically three operations that can be performed on stacks. They are:
i. inserting an item into a stack (push).
ii. deleting an item from the stack (pop). 
iii. displaying the contents of the stack(pip).
The stack abstract data type is defined by the following structure and operations. A stack is structured, as 
described above, as an ordered collection of items where items are added to and removed from the end called 
the “top.” Stacks are ordered LIFO. 
A stack can be implemented as an array in which case, it is static data structure or as a linked list which is 
dynamic data structure. A stack implemented as an array inherits all the properties of an array and if 
implemented as a linked list all characteristics of a linked list are possessed by it.
The stack operations are given below.
Stack() creates a new stack that is empty. It needs no parameters and returns an empty stack. push(item) adds 
a new item to the top of the stack. It needs the item and returns nothing.
pop() removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
peek() returns the top item from the stack but does not remove it. It needs no parameters. The stack is not 
modified.
Algorithm of peek function:
begin procedure peek
 return stack[top]
end procedure
isEmpty() tests to see whether the stack is empty. It needs no parameters and returns a boolean value.
size() returns the number of items on the stack. It needs no parameters and returns an integer.
For example, if s is a stack that has been created and starts out empty, then the table below shows the results 
of a sequence of stack operations. Under stack contents, the top item is listed at the far right.
Stack Operation Stack Contents Return Value 
s.isEmpty() [] True
s.push(4) [4]
s.push('dog') [4,'dog']
s.peek() [4,'dog'] 'dog'
s.push(True) [4,'dog',True]
s.size() [4,'dog',True] 3
s.isEmpty() [4,'dog',True] False
s.push(8.4) [4,'dog',True,8.4]
s.pop() [4,'dog', True] 8.4
s.pop() [4,'dog'] True
s.size() [4,'dog'] 2
Implementation of stack in C
#include <stdio.h>
int MAXSIZE = 8; 
int stack[8]; 
int top = -1; 
int isempty() {
 if(top == -1)
 return 1;
 else
 return 0;
}
 
int isfull() {
 if(top == MAXSIZE)
 return 1;
 else
 return 0;
}
int peek() {
 return stack[top];
}
int pop() {
 int data;
 if(!isempty()) {
 data = stack[top];
 top = top - 1; 
 return data;
 } else {
 printf("Could not retrieve data, Stack is empty.\n");
 }
}
int push(int data) {
 if(!isfull()) {
 top = top + 1; 
 stack[top] = data;
 } else {
 printf("Could not insert data, Stack is full.\n");
 }
}
int main() {
 // push items on to the stack 
 push(3);
 push(5);
 push(9);
 push(1);
 push(12);
 push(15);
 printf("Element at top of the stack: %d\n" ,peek());
 printf("Elements: \n");
 // print stack data 
 while(!isempty()) {
 int data = pop();
 printf("%d\n",data);
 }
 printf("Stack full: %s\n" , isfull()?"true":"false");
 printf("Stack empty: %s\n" , isempty()?"true":"false");
 
 return 0;
}
Output
Whenever we are trying to pop an element from an empty stack we have a stack underflow.
Whenever we are trying to push an element onto a stack and top[S] = n we have a stack overflow.
Clearly, an underflow has to be always reported as an error. For an overflow we have two choices: either to 
report it as an error or to try to work out the situation by increasing dynamically the size of the array S. 
 
Write a function to perform a PUSH operation on a dynamically allocated stack containing real number.
Solution:
struct Node
{ float Number ;
Node *Link ;
} ;
class STACK
{ Node *Top ;
public :
STACK( ) {Top = NULL ;}
void PUSH( ) ;
void POP( ) ;
~STACK( ) ;
} ;
void STACK::PUSH( )
{ Node *Temp;
Temp=new Node;
if(Temp= =NULL)
{
cout<<”\nNo memory to create the node…”;
exit(1);
}
cout<<”\nEnter the Number to be inserted: “;
cin>>Temp→ Number;
Temp→ Link=Top;
Top=Temp;
}
 
 
APPLICATION OF STACK 
Expression Evolution 
The way arithmetic expression is written is referred to as notation. An arithmetic expression can be written in 
three different but equivalent notations, i.e., without changing the essence or output of an expression. These 
notations are −
 Infix Notation 
This is the most popular and the easiest to understand of all notations. Operators are used in-between 
operands in infix notation, e.g. 
𝑎𝑎 − 𝑏𝑏 + 𝑐𝑐
Element at top of the stack: 15
Elements:
15
12
1 
9 
5 
3 
Stack full: false
Stack empty: true
Algorithm to process infix notation could however be difficult and costly in terms of time and space 
consumption.
 Prefix Notation 
In this notation, operator is prefixed to operands, i.e. operator is written ahead of operands. For 
example, +𝑎𝑎𝑎𝑎. This is equivalent to its infix notation 𝑎𝑎 + 𝑏𝑏. Prefix notation is also known as Polish 
Notation.
 Postfix Notation 
This notation style is known as Reversed Polish Notation. In this notation style, the operator is postfixed
to the operands i.e., the operator is written after the operands. For example, 𝑎𝑎𝑎𝑎 +. This is equivalent 
to its infix notation 𝑎𝑎 + 𝑏𝑏.
The following table briefly tries to show the difference in all three notations
Parsing Expressions
As we have discussed, it is not a very efficient way to design an algorithm or program to parse infix notations. 
Instead, these infix notations are first converted into either postfix or prefix notations and then computed. To 
parse any arithmetic expression, we need to take care of operator precedence and associativity also.
Precedence
When an operand is in between two different operators, which operator will take the operand first, is decided 
by the precedence of an operator over others. For example –
As multiplication operation has precedence over addition, b * c will be evaluated first. 
 
Associativity 
Associativity describes the rule where operators with the same precedence appear in an expression. For 
example, in expression a + b − c, both + and – have the same precedence, then which part of the expression 
will be evaluated first, is determined by associativity of those operators. Here, both + and − are left associative, 
so the expression will be evaluated as (a + b) − c.
Precedence and associativity determines the order of evaluation of an expression. Following is an operator 
precedence and associativity table (highest to lowest).
 
Expression conversion 
Procedure to convert Infix to Postfix
1. Scan the Infix string from left to right.
2. Initialize an empty stack.
3. If the scanned character is an operand, add it to the Postfix string.
4. If the scanned character is an operator and if the stack is empty push the character to stack.
5. If the scanned character is an Operator and the stack is not empty, compare the precedence of the character 
with the element on top of the stack.
6. If top Stack has higher precedence over the scanned character pop the stack else push the scanned character 
to stack. Repeat this step until the stack is not empty and top Stack has precedence over the character.
7. Repeat 4 and 5 steps till all the characters are scanned.
8. After all characters are scanned, we have to add any character that the stack may have to the Postfix string.
9. If stack is not empty add top Stack to Postfix string and Pop the stack.
10. Repeat this step as long as stack is not empty.
Assignment (see http://scanftree.com/Data_Structure/infix-to-postfix)
Discuss the procedure for the conversion of:
Infix to Prefix
Postfix to Infix
Prefix to Infix
Procedure to evaluate postfix notations
Infix notation is easier for humans to read and understand whereas for electronic machines like computers, 
postfix is the best form of expression to parse. Below is a program to convert and evaluate infix notation to 
postfix notation
#include
#include<stdio.h> 
#include<string.h> 
//char stack
char stack[25]; 
int top = -1; 
void push(char item) {
 stack[++top] = item; 
} 
char pop() {
 return stack[top--]; 
} 
//returns precedence of operators
int precedence(char symbol) {
 switch(symbol) {
 case '+': 
 case '-':
 return 2; 
 break; 
 case '*': 
 case '/':
 return 3; 
 break; 
 case '^': 
 return 4; 
 break; 
 case '(': 
 case ')': 
 case '#':
 return 1; 
 break; 
 } 
} 
//check whether the symbol is operator?
int isOperator(char symbol) {
 switch(symbol) {
 case '+': 
 case '-': 
 case '*': 
 case '/': 
 case '^': 
 case '(': 
 case ')':
 return 1; 
 break; 
 default:
 return 0; 
 } 
} 
//converts infix expression to postfix
void convert(char infix[],char postfix[]) {
 int i,symbol,j = 0; 
 stack[++top] = '#'; 
 for(i = 0;i<strlen(infix);i++) {
 symbol = infix[i]; 
 if(isOperator(symbol) == 0) {
 postfix[j] = symbol; 
 j++; 
 } else {
 if(symbol == '(') {
 push(symbol); 
 }else {
 if(symbol == ')') {
 while(stack[top] != '(') {
 postfix[j] = pop(); 
j++; 
 } 
 pop();//pop out (. 
 } else {
 if(precedence(symbol)>precedence(stack[top])) {
 push(symbol); 
 }else {
 while(precedence(symbol)<=precedence(stack[top])) {
 postfix[j] = pop(); 
j++; 
 } 
 push(symbol); 
 }
 }
 }
 }
 }
 while(stack[top] != '#') {
 postfix[j] = pop(); 
 j++; 
 } 
 postfix[j]='\0';//null terminate string. 
} 
//int stack
int stack_int[25]; 
int top_int = -1; 
void push_int(int item) {
 stack_int[++top_int] = item; 
} 
char pop_int() {
 return stack_int[top_int--]; 
} 
//evaluates postfix expression
int evaluate(char *postfix){
 char ch;
 int i = 0,operand1,operand2;
 while( (ch = postfix[i++]) != '\0') {
 if(isdigit(ch)) {
 push_int(ch-'0'); // Push the operand 
 }else {
 //Operator,pop two operands 
 operand2 = pop_int();
 operand1 = pop_int();
 switch(ch) {
 case '+':
 push_int(operand1+operand2);
 break;
 case '-':
 push_int(operand1-operand2);
 break;
 case '*':
 push_int(operand1*operand2);
 break;
 case '/':
 push_int(operand1/operand2);
 break;
 }
 }
 }
 return stack_int[top_int];
}
void main() { 
 char infix[25] = "1*(2+3)",postfix[25]; 
 convert(infix,postfix); 
 printf("Infix expression is: %s\n" , infix);
 printf("Postfix expression is: %s\n" , postfix);
 printf("Evaluated expression is: %d\n" , evaluate(postfix));
}
#include <stdio.h>
#include <string.h>
#define MAXSIZE 100
#define TRUE 1
#define FALSE 0 
// Structure defining Stack data structure
struct Stack {
 int top;
 int array[MAXSIZE];
} st;
/*
Initializes the top index to -1

void initialize() {
st.top = -1;
}
/*
Checks if Stack is Full or not 

int isFull() { 
 if(st.top >= MAXSIZE-1)
 return TRUE;
 else
 return FALSE;
}
/*
Checks if Stack is Empty or not

int isEmpty() {
if(st.top == -1)
 return TRUE;
else
 return FALSE;
}
/*
Adds an element to stack and then increment top index 

void push(int num) {
 if (isFull())
 printf("Stack is Full...\n");
 else {
 st.array[st.top + 1] = num;
 st.top++;
 }
}
/*
Removes top element from stack and decrement top index

int pop() {
 if (isEmpty())
 printf("Stack is Empty...\n");
 else {
 st.top = st.top - 1;
 return st.array[st.top+1];
 }
}
int main() {
 char inputString[100], c;
 int i, length;
 initialize();
 printf("Enter a string\n");
 gets(inputString);
 length = strlen(inputString);
 /* Push all characters of input String to Stack 
 for(i = 0; i < length; i++){
 push(inputString[i]);
 }
 /* Poping characters from stack returs the characters of input string
 in reverse order. We will then compare it with corresponding 
 characters of input string. If we found a mismatch the input 
 string is not a palindrome string 
 for(i = 0; i < length; i++){
 if(pop() != inputString[i]) {
 printf("Not a Palindrome String\n");
 return 0;
 }
 }
 printf("Palindrome String\n");
 return 0;
}
</string.h></stdio.h>
Check:
http://www.tutorialride.com/c-stack-programs/check-string-is-palindrome-using-stack-c-program.htm
http://www.techcrashcourse.com/2016/06/c-program-to-check-palindrome-string-using-stack.html
A program takes a string and checks whether the string is palindrome or not using stack.
http://www.sanfoundry.com/c-program-palindrome-stack/
 
Problem Solution 
1. Take a string as input.
2. Store the string in the stack array.
3. Check whether the string is palindrome or not.
Program Explanation
1. Take a string as input and store it in the array s[].
2. Load each character of the array s[] into the array stack[].
3. Use variables front and top to represent the last and top element of the array stack[].
4. Using for loop compare the top and last element of the array stack[]. If they are equal, then delete the top 
element, increment the variable front by 1 and compare again.
5. If they are not equal, then print the output as “It is not a palindrome”.
6. Compare the elements in the steps 4-5 upto the middle element of the array stack[].
7. If every characters of the array is equal, then it is a paliandrome.
/*
* C Program to Identify whether the String is Palindrome or not using Stack

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 50
int top = -1, front = 0;
int stack[MAX];
void push(char);
void pop();
void main()
{
 int i, choice;
 char s[MAX], b;
 while (1)
 {
 printf("1-enter string\n2-exit\n");
 printf("enter your choice\n");
 scanf("%d", &choice);
 switch (choice)
 {
 case 1:
 printf("Enter the String\n");
 scanf("%s", s);
 for (i = 0;s[i] != '\0';i++)
 {
 b = s[i];
 push(b);
 }
 for (i = 0;i < (strlen(s) / 2);i++)
 {
 if (stack[top] == stack[front])
 {
 pop();
front++;
 }
 else
 {
 printf("%s is not a palindrome\n", s);
 break; 
 }
 }
 if ((strlen(s) / 2) = = front)
 printf("%s is palindrome\n", s);
 front = 0;
 top = -1;
 break;
 case 2:
 exit(0);
 default:
 printf("enter correct choice\n");
 }
 }
}
/* to push a character into stack 
void push(char a)
{
 top++;
 stack[top] = a;
}
/* to delete an element in stack 
void pop()
{
 top--;
}
/*
* Java Program to Identify whether the String is Palindrome or not using Stack

import java.util.*;
//with explanations.
public class palindorme{
public static void main(String[] args){
Scanner uin = new Scanner(System.in);
//creating the stacks for the string
Stack str1 = new Stack();
Stack revStr = new Stack(); //to hold the reverse string
System.out.print("What's your test word: ");
String str = uin.next().toLowerCase(); //input the string
char[] mainStr = str.toCharArray(); //splitting the given string to individual 
characters.
//pushing the characters of the given string to the first stack.
for(int i = 0; i < mainStr.length; i++){
str1.push(mainStr[i]);
}
//pushing the reverse of the string to another stack
for(int j = 0; j < mainStr.length; j++){
revStr.push(mainStr[(mainStr.length - 1) - j]);
}
//popping the items in the original stack and comparing with the reversed stack (as 
long as the stack is not empty)
while(!str1.empty()){ //as long as the stack is not empty
if(str1.pop() == revStr.pop()){ //if the top of the reversed stack is same 
as the top of the normal stack
//check if it's the last item in the stack that just got popped.
if(str1.size() == 0){
//if it's the last item then the string is a palindrome.
System.out.println(str + " is a palindrome");
break;
} else{
continue;
}
} else { // if the top of the two stacks are not the same then automatically, 
it is not a palindrome.
System.out.println(str + " is not a palindrome");
break;
}
}
}
}
Queue is a list where insertion is done at one end and removal is done at the other end. 
Dequeue is a list where every end supports insertion and removal.
With this feature, it is possible to use the dequeue as a list and a stack at the same time as required by the 
application. 
Priority queue does not have any ends.
In a priority queue, elements can be inserted in any order but removal of the elements is in a sorted order.
Due to this behavior, a priority queue can be used to sort the elements.
Since sorting is done only when the elements are removed from the priority queue, the PQ is easily 
implemented by a heap.
Using an array-based heap, elements can be inserted and deleted in O(logN).
Dale, Nell; Walker, Henry M. (1996). Abstract Data Types: Specifications, Implementations, and Applications. 
Jones & Bartlett Learning. ISBN 978-0-66940000-7.*/
