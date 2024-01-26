/* tslint:disable */
/* eslint-disable */
/**
*/
export function main_js(): void;
/**
* @param {number} seed
* @returns {Uint32Array}
*/
export function generate_mines(seed: number): Uint32Array;
/**
* @param {number} x
* @param {number} y
* @returns {boolean}
*/
export function check_x(x: number, y: number): boolean;
/**
* @param {string} key
*/
export function add_key(key: string): void;
/**
*/
export enum TILES {
  WATER = 0,
  PLAYER = 1,
  X = 2,
  MINE = 3,
}
