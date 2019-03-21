class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SList {
  constructor() {
    this.head = null;
    this.len = 0;
  }

  addFront(val) {
    var newNode = new Node(val);
    newNode.next = this.head;
    this.head = newNode;
    this.len++;
    return this;
  }

  removeFront() {
    if(this.head) {
      this.head = this.head.next;
      this.len--;
    }
    return this;
  }

  contains(val) {
    var currentNode = this.head;
    while(currentNode) {
      if(val === currentNode.val) {
        return true;
      }
      currentNode = currentNode.next;
    }
    return false;
  }

  length() {
    var count = 0;
    var curr = this.head;
    while(curr) {
      count++;
      curr = curr.next;
    }
    return count;
  }

  max() {
    // if(this.head) {
    //   var max = this.head.val;
    // } else {
    //   var max = null;
    // }
    var max = this.head ? this.head.val : null;
    var curr = this.head;
    while(curr) {
      if(curr.val > max) {
        max = curr.val;
      }
      curr = curr.next;
    }
    return max;
  }

  display() {
    var result = [];
    var curr = this.head;
    while(curr){
      result.push(curr.val);
      curr = curr.next;
    }
    console.log(result);
    return this;
  }
}

var list = new SList();
list.addFront("D").addFront("C").addFront("B").addFront("a").display();
// console.log(list.contains("A"));
// console.log(list.contains("Z"));
console.log(list.max());

// console.log([1, 2, 3, 4].length);

// falsey values in js
// null, undefined, false, 0

// falsey values in python
// None, False, 0, [], "", {}