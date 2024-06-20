#!/usr/bin/node

/**
 * Converts a number to a string representation in the specified base.
 * @param {number} base - The base to convert the number to.
 * @returns {function} - A function that takes a number and converts it to a string representation in the specified base.
 */
exports.converter = function converter(base) {
  /**
   * Converts a number to a string representation in the specified base.
   * @param {number} num - The number to be converted.
   * @returns {string} - The string representation of the number in the specified base.
   */
  return function (num) {
    num = num.toString(base);
    return num;
  };
};
