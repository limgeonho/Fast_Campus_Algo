# 두개의 손
# 뭔가 하나의 사이클이나 같은 행동을 상황에 따라 다르게 돌아가면서 하는 경우 % 연산을 생각하자(달팽이문제, )

ML, MR, TL, TR = ('SPR'.index(i) for i in input().split())

if ML == MR and (ML + 2) % 3 in [TL, TR]:
    print('TK')
elif TL == TR and (TL + 2) % 3 in [ML, MR]:
    print('MS')
else:
    print('?')

# # 둘다 다를 경우
# if ML != MR and TL != TR:
#     print("?")
#
# # MS만 같을 경우
# elif ML == MR and TL != TR:
#     if ML == 'S' and (TL == 'R' or TR == 'R'):
#         print("TK")
#     elif ML == 'P' and (TL == 'S' or TR == 'S'):
#         print("TK")
#     elif ML == 'R' and (TL == 'P' or TR == 'P'):
#         print("TK")
#     else:
#         print("?")
#
# # TK만 같을 경우
# elif ML != MR and TL == TR:
#     if TL == 'S' and (ML == 'R' or MR == 'R'):
#         print("MS")
#     elif TL == 'P' and (ML == 'S' or MR == 'S'):
#         print("MS")
#     elif TL == 'R' and (ML == 'P' or MR == 'P'):
#         print("MS")
#     else:
#         print("?")
#
# # 둘다 같을 경우
# else:
#     if ML == 'S':
#         if TL == 'P':
#             print("MS")
#         if TL == 'S':
#             print("?")
#         if TL == 'R':
#             print("TK")
#     if ML == 'R':
#         if TL == 'P':
#             print("TK")
#         if TL == 'S':
#             print("MS")
#         if TL == 'R':
#             print("?")
#     if ML == 'P':
#         if TL == 'P':
#             print("?")
#         if TL == 'S':
#             print("TK")
#         if TL == 'R':
#             print("MS")