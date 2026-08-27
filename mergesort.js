let a = [1, 3, 645, 45]
let n = a.length
function mergesort(a, left, right) {
    if (left < right) {
        let mid = Math.floor(left + (right - left) / 2)

        mergesort(a, left, mid)       
        mergesort(a, mid + 1, right) 
        merge(a, left, mid, right)   
    }
}
function merge(arr, left, mid, right) {
    let leftArr = arr.slice(left, mid + 1)  gf
    let rightArr = arr.slice(mid + 1, right + 1)
    let i = 0, j = 0, k = left   
    while (i < leftArr.length && j < rightArr.length) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i]
            i++
        } else {
            arr[k] = rightArr[j]
            j++
        }
        k++
    }
    while (i < leftArr.length) {
        arr[k] = leftArr[i]
        i++
        k++
    }
    while (j < rightArr.length) {
        arr[k] = rightArr[j]
        j++
        k++
    }}
mergesort(a, 0, n - 1)
console.log(a)  
