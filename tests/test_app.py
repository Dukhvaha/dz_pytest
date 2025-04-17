# import pytest
#
#
# class TestMathOperations():
#     @pytest.mark.paramentrize("x,y,res",[
#                                   (2,3,6),
#                                   (2,'1',2)
#     ])
#     def test_multiply(self,x,y,res):
#         assert MathOperations().multiply(x,y) == res
#
#     @pytest.mark.paramentrize("x,y,res",[
#                                   (4,2,16),
#                                   (2,0,1),
#                                   (2,'1',2)
#     ])
#     def test_power(self,x,y,res):
#         assert MathOperations().power(x,y) == res
#
#     @pytest.mark.paramentrize("x,res",[
#                                   (4,2),
#                                   (0,0),
#                                   (-4, 2)
#     ])
#     def test_sqlt(self,x, res):
#         assert MathOperations().sqrt(x,) == res