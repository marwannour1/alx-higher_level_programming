#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle') {
  constructor(size) {
    super(size, size);
  }
  charPrint(c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
