

//use for loop : when no. of iteration is known 
//use while loop : when no. of iteration is not known
let array = [12, 23, 4, 5, 67]
let n = array.length

for (let i = 0; i < n; i++) {
    let key = array[i]      
    let j = i - 1
    while (j >= 0 && array[j] > key) {  
        array[j + 1] = array[j]
        j--
    }
    array[j + 1] = key         
}

console.log(array)
