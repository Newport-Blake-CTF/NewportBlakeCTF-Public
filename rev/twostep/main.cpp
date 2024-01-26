#include <iostream>
#include <string>

static union forward {
    size_t fi;
    double fd;
} ff;

using namespace std;
bool onestep(const char* s);
bool twostep(const char* s);

static size_t count = 0;
static short nums[] = {4, 7, 2, 0, 3, 6, 5, 1, 8};
static int threestep[] = {0, 0, 0, 0, 0};

// nbctf{L3f7_f0rw4Rd_r1gh7_rIghT_l3FT_1n_RigH7_b4cK_return}
inline const char* next(const char* s) {
    size_t i = nums[count++];
    while (i) { 
        s++;
        if (*s == '}' || *s == '\0') {
            cout << "Aww shucks!" << endl;
            exit(1);
        }
        if (*s == '_') {
            s++;
            i--;
        }
    }
    return s;
}

bool onestep(const char* s) {
    const char* t;
    short nums[] = {18440, 3136, 18444, 16524};
    size_t n[] = {1, 16, 32, 512, 1024, 2048, 8192, 16384};
    size_t i = 0;
    size_t r[] = {177, 166, 183, 182, 177, 173};
    short h, b;
    char f[] = {'\xaa', 0};
    switch (count) {
        case 0:
            if (s[0] != 'n' || s[1] != 'b' || s[2] != 'c' || s[3] != 't' || s[4] != 'f' || s[5] != '{') {
                return false;
            }
            return twostep(s + 6);
        case 1:
            t = next(s);
            for (i = 0; i < 4; i++) {
                char c = t[i];
                short n = 0;
                for (size_t j = 0; j < 4; j++) {
                    n |= (c & 0x3) << (j * 4 + 2);
                    c >>= 2;
                }
                if (n != nums[i]) {
                    return false;
                }
            }
            return twostep(s);
        case 3:
            t = next(s);
            for (i = 0; i < 5; i++) {
                threestep[i] = t[i];
            }
            return twostep(s);
        case 6:
            t = next(s);
            h = *(short*)t;
            i = 0;
            while (h) {
                b = h & (~h + 1);
                if (i == 8) return false;
                if (n[i] == b) {
                    i++;
                }
                h ^= b;
            }
            return i == 8 ? twostep(s) : false;
        case 8: 
            t = next(s);
            for (i = 0; i < 6; i++) {
                f[0] = t[i] ^ r[i];
                (*((int(*)())f))();
            }
            return true;
    }
    return false;
}

bool twostep(const char* s) {
    const char* t;
    size_t i = 0;
    size_t r[] = {54515, 15689, 4219, 50297, 43652, 38919};
    size_t a[] = {14668, 24063, 37349, 50716, 61563};
    size_t x[] = {1843061, 222420, 5184810, 4590105, 2184197};
    size_t v = 0;
    size_t n[] = {1073741834, 2415919110, 939524099, 536870913, 1845493760};
    switch (count) {
        case 0:
            t = next(s);
            // 4, 91, 46, 60
            if ((t[0] ^ 4) != (t[1] ^ 91) ||
                (t[1] ^ 91) != (t[2] ^ 46) ||
                (t[2] ^ 46) != (t[3] ^ 60) ||
                (t[3] ^ 60) != (t[0] ^ 4) ||
                (t[0] ^ 4) != 0x68) {
                return false;
            }
            return onestep(s);
        case 2:
            t = next(s);
            for (i = 0; i < 5; i++) {
                if (t[i] * r[i + 1] + r[i] != x[i]) {
                    return false;
                }
            }
            return onestep(s);
        case 4:
            t = next(s);
            for (i = 0; i < 5; i++) {
                v += threestep[i] + 128 * t[i];
                if (v != a[i]) {
                    return false;
                }
            }
            return twostep(s);
        case 5:
            t = next(s);
            for (i = 0; i < 5; i++) {
                v = i + 3;
                if (n[i] != (uint)(t[i] >> v | t[i] << (32 - v))) {
                    return false;
                }
            }
            return onestep(s);
        case 7:
            t = next(s);
            ff.fi = *(size_t*)t;
            return ff.fd == 3.3259470343420984e+151 ? onestep(s) : false;
    }
    return false;
}

int main() {
    string s;
    cout << "C'mon y'all let's boogie!\n> " << flush;
    cin >> s;
    if (s.length() == 57 && onestep(s.c_str())) {
        cout << "Yeehaw!" << endl;
    } else {
        cout << "Aww shucks!" << endl;
    }
}