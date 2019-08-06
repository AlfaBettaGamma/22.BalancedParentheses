def recParenthese(output, open, close, N,res):
  if open == N and close == N:
    res.append(output)
  else:
    if open < N:
      recParenthese(output + '(', open + 1, close, N,res)
    if close<open:
      recParenthese(output + ')', open, close + 1, N,res)
  return res


def BalancedParentheses(N):
  res = []
  result = ''
  res = recParenthese('', 0, 0, N,res)
  result = ' '.join(res)
  return result

# порядок последовательностей скобок начиная с 0 : 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452, 18367353072152, 69533550916004, 263747951750360, 1002242216651368, 3814986502092304
#print(BalancedParentheses(2))
#print(BalancedParentheses(3))
#print(BalancedParentheses(4))
#print(BalancedParentheses(5))
#print(BalancedParentheses(6))
#print(BalancedParentheses(7))
#print(BalancedParentheses(8))
#print(BalancedParentheses(9))