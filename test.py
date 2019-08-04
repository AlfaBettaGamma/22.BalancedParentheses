def recParentheses(N, paren=None):
  if N == 1:
    res = ['()']
    return res
  else:
      if paren == 1:
        return ["()" * N]
      else:
        if not paren:
          paren = N
        string = "".join(["(" * paren, ")" * paren])
        if paren < N:
          string += "()" * (N-paren)
        return [string] + recParentheses(N, paren-1)

def BalancedParentheses(N):
  res = ''
  result = ''
  res = recParentheses(N, paren=None)
  for i in range(len(res)):
    result = result + res[i] +' '
  return result

print(BalancedParentheses(2))
print(BalancedParentheses(3))
print(BalancedParentheses(4))
print(BalancedParentheses(5))
print(BalancedParentheses(6))
print(BalancedParentheses(7))
print(BalancedParentheses(8))
print(BalancedParentheses(9))