"""class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        volume=0
        left, right = 0, len(height)-1
        left_max,right_max= height[left],height[right]

        while left < right:
            left_max, right_max = max(height[left],left_max), max(height[right],right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left+=1

            else:
                volume += right_max -height[right]
                right -=1

        return volume

height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol=Solution()
print(sol.trap(height))
"""
#height=[4,2,0,3,2,5]
"""height=[4,2,0,3,2,5]
num=max(height)
#li=[[False]*num]*len(height) 이걸로 했을 시 잘 되지 않음
li=[[0]*num for i in range(len(height))]
abc=0
for i in range(len(height)):
    for j in range(num):
        if j < height[i]:
            li[i][j]=True
        else:
            li[i][j]=False
print('\n'.join(map(str,li)))
print(li[0][1])"""

"""        if li[i][j] == True:
            num+=1
print(num)"""

class Solution:
    def trap(self, height: list[int]) -> int:
        stack=[]
        volume =0

        for i in range(len(height)):
            #변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                #print(stack)
                #스택에서 꺼낸다.
                top=stack.pop()
                if not len(stack):
                    break
                distance = i -stack[-1]-1
                waters=min(height[i],height[stack[-1]])-height[top]
                #print('d:',distance,'w:',waters)
                volume+=distance* waters
            stack.append(i)
        return volume

height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol=Solution()
print(sol.trap(height))

