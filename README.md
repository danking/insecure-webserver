(don't) try this:

```
cat >foo.c <<EOF
int add(int a, int b) {
    return a + b;
}

int run() {
    return add(3, 5);
}
EOF
clang -shared foo.c -o foo.so
curl -XPOST 127.0.0.1:5000/ --data-binary @foo.so
```
