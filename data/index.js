class PowerOfTwoMaxHeap {
    constructor(childrenPower) {
        this.childrenPower = childrenPower;
        this.heap = [];
    }

    getParentIndex(index) {
        return Math.floor((index - 1) / Math.pow(2, this.childrenPower));
    }

    getChildIndices(index) {
        let start = index * Math.pow(2, this.childrenPower) + 1;
        let end = start + Math.pow(2, this.childrenPower);
        let indices = [];
        for (let i = start; i < end; i++) {
            indices.push(i);
        }
        return indices;
    }

    insert(value) {
        this.heap.push(value);
        this.heapifyUp(this.heap.length - 1);
    }

    heapifyUp(index) {
        let parentIndex = this.getParentIndex(index);
        while (index > 0 && this.heap[index] > this.heap[parentIndex]) {
            [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
            index = parentIndex;
            parentIndex = this.getParentIndex(index);
        }
    }

    popMax() {
        if (this.heap.length === 0) return null;
        let max = this.heap[0];
        this.heap[0] = this.heap.pop();
        this.heapifyDown(0);
        return max;
    }

    heapifyDown(index) {
        let childIndices = this.getChildIndices(index);
        while (true) {
            let largest = index;
            for (let i of childIndices) {
                if (i < this.heap.length && this.heap[i] > this.heap[largest]) {
                    largest = i;
                }
            }
            if (largest !== index) {
                [this.heap[index], this.heap[largest]] = [this.heap[largest], this.heap[index]];
                index = largest;
                childIndices = this.getChildIndices(index);
            } else {
                break;
            }
        }
    }
}

// Example usage:
let heap = new PowerOfTwoMaxHeap(2); // Each parent has 2^2 = 4 children
heap.insert(10);
heap.insert(20);
heap.insert(30);
heap.insert(5);
console.log(heap.popMax()); // 30
console.log(heap.popMax()); // 20
console.log(heap.popMax()); // 10
console.log(heap.popMax()); // 5
