class FreqStack:

    def __init__(self):
        self.freq=defaultdict(int) # maps val->freq_count
        self.group=defaultdict(list) #maps freq_count->[values]
        self.max_freq=0 #track of max frequency

    def push(self, val: int) -> None:
        f=self.freq.get(val,0)+1
        self.freq[val]=f
        if f>self.max_freq:
            self.max_freq=f
        self.group[f].append(val)

    def pop(self) -> int:
        val=self.group[self.max_freq].pop()
        self.freq[val]-=1

        if not self.group[self.max_freq]:
            self.max_freq-=1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()