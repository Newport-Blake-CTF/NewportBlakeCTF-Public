import "./App.css";
import Game from "./Game";
import { useEffect } from "react";

function App() {
    // in case this isn't obvious, I find this very amusing
    let bgm = new Audio("/bgm.ogg");
    bgm.volume = 0.03;
    bgm.loop = true;
    bgm.play();

    const handleKeyDown = (event) => {
        const { key } = event;
        if (key === "m") {
            if (bgm.paused) {
                bgm.play();
            } else {
                bgm.pause();
                console.log("you can't escape...");
                setTimeout(() => {
                    bgm.play();
                    bgm.volume += 0.01;
                }, 3000);
            }
        }
    }

    useEffect(() => {
        document.title = "flotsam ~ drifting along in the aimless sea ~";
        window.addEventListener("keydown", handleKeyDown);
        return () => {
            window.removeEventListener("keydown", handleKeyDown);
        };
    });

    return (
        <div className="App">
            <main className="App-main">
                <Game />
            </main>
        </div>
    );
}

export default App;
