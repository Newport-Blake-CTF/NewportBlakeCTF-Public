import "./Game.css";
import { useState, useEffect, useRef } from "react";
const flotsam = await import("flotsam");

const BOARD_SIZE = 99;
const TILES = flotsam.TILES;
const TILE_MAPPING = {
    [TILES.WATER]: "🌊",
    [TILES.PLAYER]: "⛵", 
    [TILES.MINE]: "💣",
    [TILES.X]: "🚩",
};
const MINES = new Set(flotsam.generate_mines(Math.round(Date.now() / 1000)));

function Game() {
    const [x, setX] = useState(0);
    const [y, setY] = useState(0);
    const [mark_flag, setXFlag] = useState(false);
    const [mark_pos, setXPos] = useState([0, 0]);

    const xRef = useRef(x);
    const yRef = useRef(y);
    const handleKeyDown = (event) => {
        const { key } = event;
        flotsam.add_key(key);
        if (key === "w" && yRef.current > 0) {
            yRef.current--;
            setY(yRef.current);
        } else if (key === "a" && xRef.current > 0) {
            xRef.current--;
            setX(xRef.current);
        } else if (key === "s" && yRef.current < 99) {
            yRef.current++;
            setY(yRef.current);
        } else if (key === "d" && xRef.current < 99) {
            xRef.current++;
            setX(xRef.current);
        } else if (key === "x") {
            if (flotsam.check_x(xRef.current, yRef.current)) {
                setXFlag(true);
                setXPos([xRef.current, yRef.current]);
            }
            else {
                alert("Try again!");
            }   
        }

        if (MINES.has(yRef.current * BOARD_SIZE + xRef.current)) {
            alert("you died!!!!");
            window.location.reload();
        }
    };

    useEffect(() => {
        window.addEventListener("keydown", handleKeyDown);
        return () => {
            window.removeEventListener("keydown", handleKeyDown);
        };
    }, []);

    const grid = [];
    for (let i = 0; i < BOARD_SIZE; i++) {
        const row = [];
        for (let j = 0; j < BOARD_SIZE; j++) {
            if (MINES.has(i * BOARD_SIZE + j)) {
                row.push(TILES.MINE);
            } else {
                row.push(TILES.WATER);
            }
        }
        grid.push(row);
    }

    grid[y][x] = TILES.PLAYER;

    if (mark_flag) {
        grid[mark_pos[1]][mark_pos[0]] = TILES.X;
    }

    return (
        <div className="Game">
            <div className="Game-grid">
                {grid.map((row, i) => (
                    <div key={i} className="Game-row">
                        {row.map((tile, j) => (
                            <div
                                key={j}
                                className={
                                    "Game-tile" +
                                    (i === y && j === x
                                        ? " Game-tile-selected"
                                        : "")
                                }
                            >
                                {TILE_MAPPING[tile]}
                            </div>
                        ))}
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Game;
