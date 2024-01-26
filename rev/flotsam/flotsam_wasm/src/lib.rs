use wasm_bindgen::prelude::*;
use web_sys::console;
use sha2::{Sha256, Digest};

#[wasm_bindgen]
extern "C" {
    fn alert(s: &str);
}

#[wasm_bindgen(start)]
pub fn main_js() -> Result<(), JsValue> {
    // This provides better error messages in debug mode.
    // It's disabled in release mode so it doesn't bloat up the file size.
    console_error_panic_hook::set_once();
    console::log_1(&"WASM loaded".into());
    Ok(())
}

#[wasm_bindgen]
pub enum TILES {
    WATER,
    PLAYER,
    X,
    MINE,
}

static mut SEED: u64 = 0;
fn _prng() -> u64 {
    let a: u64 = 0x235342474C4F;
    let c: u64 = 0x56334C434753;

    unsafe {
        SEED = a.wrapping_mul(SEED).wrapping_add(c);
        SEED
    }   
}

#[wasm_bindgen]
pub fn generate_mines(seed: u32) -> Vec<u32> {
    let mut mine: Vec<u32> = Vec::new();
    unsafe {
        SEED = seed as u64;
    }
    for _ in 0..300   {
        let x = _prng() % 99;
        let y = _prng() % 99;
        mine.push((x * 99 + y) as u32);
    }
    mine
}

fn flag_1() -> String {
    let enc = b"\xee\xe3\xe1\xf7\xe2\xfe\xf1\xb4\xe4\xea\xba\xe6\xe9\xd2\xbc\xd0\xe4\xf9\xa1\xcc\xe3\xa5\xe4\xa6\xfc\xc6\xaa\xfd\xc3\xea\xaa\xec\xcd\xdc";

    let mut dec = String::with_capacity(34);
    for i in 0..34 {
        dec.push((enc[i] ^ (0x80 + i as u8)) as char);
    }

    dec
}

#[wasm_bindgen]
pub fn check_x(x: u32, y: u32) -> bool {
    unsafe {
        let sxy = SEED % 9801;
        if x * 99 + y == sxy as u32 {
            alert(format!("You found the secret treasure! {}", flag_1()).as_str());
            return true;
        }
        false
    }
}


static mut KEY_EVENTS: Vec<String> = Vec::new();
static C: [&str; 12] = [
    "BsspxEpxo", "BsspxEpxo", "BsspxVq", "BsspxVq",  "BsspxSjhiu",  "BsspxMfgu", "BsspxSjhiu", "BsspxMfgu", "b", "c", "Tijgu", "Foufs"
];
static FLAG2: &[u8; 54] = b"\xc9D\xc5\xa8S\xacei\x81\xe85\x99\xcf#}\x9d\xb4\xe8\xa8\xb3\xdc\x89\xf4R\x12h\x17\xa2*fK \xc8S\xf9\xbfT\xb9Yv\x85\xe5*\x99\xc3\"F\x8f\x8a\xe9\xa3\xad\x9d\x97";

#[wasm_bindgen]
pub fn add_key(key: &str) -> Result<(), JsValue> {
    unsafe {
        let mut _key = String::from(key);
        for i in 0..key.len() {
            _key.as_bytes_mut()[i] = key.as_bytes()[i] + 1;
        }

        KEY_EVENTS.push(_key);
        if KEY_EVENTS.len() > 12 {
            KEY_EVENTS.remove(0);
        }
        
        for i in 0..KEY_EVENTS.len() {
            if KEY_EVENTS[i] != C[i] {
                KEY_EVENTS.clear();
                return Ok(());
            }
        }

        if KEY_EVENTS.len() != 12 {
            return Ok(());
        }

        let mut code = String::new();
        for key in KEY_EVENTS.iter() {
            code.push_str(key);
        }
        
        let mut hasher = Sha256::new();
        hasher.update(code);
        let result = hasher.finalize();

        let mut dec = String::with_capacity(54);
        for i in 0..54 {
            dec.push((result[i % 32] ^ FLAG2[i]) as char);
        }

        console::log_1(&"Cheat code activated!".into());
        console::log_1(&dec.into());

        KEY_EVENTS.clear();
        Ok(())
    }
}