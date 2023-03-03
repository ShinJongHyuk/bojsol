import sys
sys.stdin = open('input.txt')







# def diagonal(i,j):
#     global diag_lst, diag_lst2
#     cnt = 0
#     cnt2 = 0
#     while 0 <= i < 19 and 0 <= j < 19:
#         if arr[i][j] == 1:
#             cnt += 1
#         elif arr[i][j] == 0:
#             if cnt != 0:
#                 diag_lst.append(cnt)
#             cnt = 0
#
#         if arr[i][j] == 2:
#             cnt2 += 1
#         elif arr[i][j] == 0:
#             if cnt2 != 0:
#                 diag_lst2.append(cnt2)
#             cnt2 = 0
#         i += 1
#         j += 1
#     return
#
# def rediagonal(i,j):
#     global rediag_lst, rediag_lst2
#     recnt = 0
#     recnt2 = 0
#     while 0 <= i < 19 and 0 <= j < 19:
#         if arr[i][j] == 1:
#             recnt += 1
#         elif arr[i][j] == 0:
#             if recnt != 0:
#                 rediag_lst.append(recnt)
#             recnt = 0
#
#         if arr[i][j] == 2:
#             recnt2 += 1
#         elif arr[i][j] == 0:
#             if recnt2 != 0:
#                 rediag_lst2.append(recnt2)
#             recnt2 = 0
#         i -= 1
#         j += 1
#     return
#
#
#
# arr = [list(map(int,input().split())) for _ in range(19)]
#
# row_lst = []
# col_lst = []
# row_lst2 = []
# col_lst2 = []
# diag_lst = []
# diag_lst2 = []
# rediag_lst = []
# rediag_lst2 = []
#
# for i in range(19):
#     row1 = 0
#     row2 = 0
#     col1 = 0
#     col2 = 0
#     for j in range(19):
#         if arr[i][j] == 1:
#             row1 += 1
#         elif arr[i][j] == 2:
#             row2 += 1
#         elif arr[i][j] == 0:
#             row_lst.append(row1)
#             row_lst2.append(row2)
#             row1 = 0
#             row2 = 0
#
#         if arr[j][i] == 1:
#             col1 += 1
#         elif arr[j][i] == 2:
#             col2 += 1
#         elif arr[j][1] == 0:
#             col_lst.append(col1)
#             col_lst2.append(col2)
#             col1 = 0
#             col2 = 0
#
# for i in range(19):
#     diagonal(i,0)
#     diagonal(0,i)
# for i in range(19):
#     rediagonal(i,0)
#     rediagonal(18,i)
#
#
# a = set(col_lst)
# c = set(row_lst)
# e = set(diag_lst)
# g = set(rediag_lst)
#
# b = set(col_lst2)
# d = set(row_lst2)
# f = set(diag_lst2)
# h = set(rediag_lst2)
#
# print(a,b,c,d,e,f,g,h)
#
# if 5 in a or c or e or g:
#     print(1)
# if 5 in b or d or f or h:
#     print(2)