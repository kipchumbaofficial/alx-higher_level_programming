#!/usr/bin/node

// A squre

const Square = require('./5-square');

class Square extends Square {
    constructor () {
        super();
    }
    printChar(c) {
        if (!c) {
            this.print()
        }
        else
