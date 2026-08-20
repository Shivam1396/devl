let a = [1, 3, 2, 5, 7, 6, 8];
let n = a.length;
//for increasing order
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n - i - 1; j++) {
    if (a[j] > a[j + 1]) {
      let temp = a[j];
      a[j] = a[j + 1];
      a[j + 1] = temp;
    }
  }
}

console.log(a);

//for decreasing order

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n - i - 1; j++) {
    if (a[j] < a[j + 1]) {
      let temp = a[j];
      a[j] = a[j + 1];
      a[j + 1] = temp;
    }
  }
}

console.log(a);

