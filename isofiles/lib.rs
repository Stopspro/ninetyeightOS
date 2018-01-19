#![allow(unused_variables)]
#![feature(lang_items)]
#![no_std]

fn main() {
#[no_mangle]
pub extern fn kmain() -> ! {

    loop { }
}
}

#[lang = "eh_personality"]
extern fn eh_personality() {
}

#[lang = "panic_fmt"]
extern fn rust_begin_panic() -> ! {
    loop {}
}
}
