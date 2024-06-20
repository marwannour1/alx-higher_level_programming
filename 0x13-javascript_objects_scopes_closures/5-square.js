#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  constructor(size) {
    super(size, size);
  }
};
