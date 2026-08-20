

//use for loop : when no. of iteration is known 
//use while loop : when no. of iteration is not known
let a = [12, 23, 4, 5, 67]
let n = a.length

for (let i = 0; i < n; i++) {
    let key = a[i]      
    let j = i - 1
    while (j >= 0 && a[j] > key) {  
        a[j + 1] = a[j]
        j--
    }
    a[j + 1] = key         
}

console.log(a)