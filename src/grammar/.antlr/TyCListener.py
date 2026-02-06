# Generated from c:/Long/Studying/School/PPL/BTL3/tyc-compiler-2252441-hk252/src/grammar/TyC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TyCParser import TyCParser
else:
    from TyCParser import TyCParser

# This class defines a complete listener for a parse tree produced by TyCParser.
class TyCListener(ParseTreeListener):

    # Enter a parse tree produced by TyCParser#program.
    def enterProgram(self, ctx:TyCParser.ProgramContext):
        pass

    # Exit a parse tree produced by TyCParser#program.
    def exitProgram(self, ctx:TyCParser.ProgramContext):
        pass


    # Enter a parse tree produced by TyCParser#declarationList.
    def enterDeclarationList(self, ctx:TyCParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by TyCParser#declarationList.
    def exitDeclarationList(self, ctx:TyCParser.DeclarationListContext):
        pass


    # Enter a parse tree produced by TyCParser#declaration.
    def enterDeclaration(self, ctx:TyCParser.DeclarationContext):
        pass

    # Exit a parse tree produced by TyCParser#declaration.
    def exitDeclaration(self, ctx:TyCParser.DeclarationContext):
        pass


    # Enter a parse tree produced by TyCParser#structDecl.
    def enterStructDecl(self, ctx:TyCParser.StructDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#structDecl.
    def exitStructDecl(self, ctx:TyCParser.StructDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#structMemberList.
    def enterStructMemberList(self, ctx:TyCParser.StructMemberListContext):
        pass

    # Exit a parse tree produced by TyCParser#structMemberList.
    def exitStructMemberList(self, ctx:TyCParser.StructMemberListContext):
        pass


    # Enter a parse tree produced by TyCParser#structMember.
    def enterStructMember(self, ctx:TyCParser.StructMemberContext):
        pass

    # Exit a parse tree produced by TyCParser#structMember.
    def exitStructMember(self, ctx:TyCParser.StructMemberContext):
        pass


    # Enter a parse tree produced by TyCParser#funcDecl.
    def enterFuncDecl(self, ctx:TyCParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by TyCParser#funcDecl.
    def exitFuncDecl(self, ctx:TyCParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by TyCParser#paramList.
    def enterParamList(self, ctx:TyCParser.ParamListContext):
        pass

    # Exit a parse tree produced by TyCParser#paramList.
    def exitParamList(self, ctx:TyCParser.ParamListContext):
        pass


    # Enter a parse tree produced by TyCParser#paramListSub.
    def enterParamListSub(self, ctx:TyCParser.ParamListSubContext):
        pass

    # Exit a parse tree produced by TyCParser#paramListSub.
    def exitParamListSub(self, ctx:TyCParser.ParamListSubContext):
        pass


    # Enter a parse tree produced by TyCParser#param.
    def enterParam(self, ctx:TyCParser.ParamContext):
        pass

    # Exit a parse tree produced by TyCParser#param.
    def exitParam(self, ctx:TyCParser.ParamContext):
        pass


    # Enter a parse tree produced by TyCParser#primitive.
    def enterPrimitive(self, ctx:TyCParser.PrimitiveContext):
        pass

    # Exit a parse tree produced by TyCParser#primitive.
    def exitPrimitive(self, ctx:TyCParser.PrimitiveContext):
        pass


    # Enter a parse tree produced by TyCParser#returnType.
    def enterReturnType(self, ctx:TyCParser.ReturnTypeContext):
        pass

    # Exit a parse tree produced by TyCParser#returnType.
    def exitReturnType(self, ctx:TyCParser.ReturnTypeContext):
        pass


    # Enter a parse tree produced by TyCParser#statement.
    def enterStatement(self, ctx:TyCParser.StatementContext):
        pass

    # Exit a parse tree produced by TyCParser#statement.
    def exitStatement(self, ctx:TyCParser.StatementContext):
        pass


    # Enter a parse tree produced by TyCParser#varDeclStmt.
    def enterVarDeclStmt(self, ctx:TyCParser.VarDeclStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#varDeclStmt.
    def exitVarDeclStmt(self, ctx:TyCParser.VarDeclStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#varInit.
    def enterVarInit(self, ctx:TyCParser.VarInitContext):
        pass

    # Exit a parse tree produced by TyCParser#varInit.
    def exitVarInit(self, ctx:TyCParser.VarInitContext):
        pass


    # Enter a parse tree produced by TyCParser#blockStmt.
    def enterBlockStmt(self, ctx:TyCParser.BlockStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#blockStmt.
    def exitBlockStmt(self, ctx:TyCParser.BlockStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#stmtList.
    def enterStmtList(self, ctx:TyCParser.StmtListContext):
        pass

    # Exit a parse tree produced by TyCParser#stmtList.
    def exitStmtList(self, ctx:TyCParser.StmtListContext):
        pass


    # Enter a parse tree produced by TyCParser#assignStmt.
    def enterAssignStmt(self, ctx:TyCParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#assignStmt.
    def exitAssignStmt(self, ctx:TyCParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#object.
    def enterObject(self, ctx:TyCParser.ObjectContext):
        pass

    # Exit a parse tree produced by TyCParser#object.
    def exitObject(self, ctx:TyCParser.ObjectContext):
        pass


    # Enter a parse tree produced by TyCParser#ifStmt.
    def enterIfStmt(self, ctx:TyCParser.IfStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#ifStmt.
    def exitIfStmt(self, ctx:TyCParser.IfStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#elseStmt.
    def enterElseStmt(self, ctx:TyCParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#elseStmt.
    def exitElseStmt(self, ctx:TyCParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#whileStmt.
    def enterWhileStmt(self, ctx:TyCParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#whileStmt.
    def exitWhileStmt(self, ctx:TyCParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#forStmt.
    def enterForStmt(self, ctx:TyCParser.ForStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#forStmt.
    def exitForStmt(self, ctx:TyCParser.ForStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#forInit.
    def enterForInit(self, ctx:TyCParser.ForInitContext):
        pass

    # Exit a parse tree produced by TyCParser#forInit.
    def exitForInit(self, ctx:TyCParser.ForInitContext):
        pass


    # Enter a parse tree produced by TyCParser#optExpr.
    def enterOptExpr(self, ctx:TyCParser.OptExprContext):
        pass

    # Exit a parse tree produced by TyCParser#optExpr.
    def exitOptExpr(self, ctx:TyCParser.OptExprContext):
        pass


    # Enter a parse tree produced by TyCParser#switchStmt.
    def enterSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#switchStmt.
    def exitSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#clauseList.
    def enterClauseList(self, ctx:TyCParser.ClauseListContext):
        pass

    # Exit a parse tree produced by TyCParser#clauseList.
    def exitClauseList(self, ctx:TyCParser.ClauseListContext):
        pass


    # Enter a parse tree produced by TyCParser#clause.
    def enterClause(self, ctx:TyCParser.ClauseContext):
        pass

    # Exit a parse tree produced by TyCParser#clause.
    def exitClause(self, ctx:TyCParser.ClauseContext):
        pass


    # Enter a parse tree produced by TyCParser#breakStmt.
    def enterBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#breakStmt.
    def exitBreakStmt(self, ctx:TyCParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#continueStmt.
    def enterContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#continueStmt.
    def exitContinueStmt(self, ctx:TyCParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#returnStmt.
    def enterReturnStmt(self, ctx:TyCParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#returnStmt.
    def exitReturnStmt(self, ctx:TyCParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#exprStmt.
    def enterExprStmt(self, ctx:TyCParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#exprStmt.
    def exitExprStmt(self, ctx:TyCParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#expression.
    def enterExpression(self, ctx:TyCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by TyCParser#expression.
    def exitExpression(self, ctx:TyCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by TyCParser#assignExpr.
    def enterAssignExpr(self, ctx:TyCParser.AssignExprContext):
        pass

    # Exit a parse tree produced by TyCParser#assignExpr.
    def exitAssignExpr(self, ctx:TyCParser.AssignExprContext):
        pass


    # Enter a parse tree produced by TyCParser#orExpr.
    def enterOrExpr(self, ctx:TyCParser.OrExprContext):
        pass

    # Exit a parse tree produced by TyCParser#orExpr.
    def exitOrExpr(self, ctx:TyCParser.OrExprContext):
        pass


    # Enter a parse tree produced by TyCParser#orExprTail.
    def enterOrExprTail(self, ctx:TyCParser.OrExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#orExprTail.
    def exitOrExprTail(self, ctx:TyCParser.OrExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#andExpr.
    def enterAndExpr(self, ctx:TyCParser.AndExprContext):
        pass

    # Exit a parse tree produced by TyCParser#andExpr.
    def exitAndExpr(self, ctx:TyCParser.AndExprContext):
        pass


    # Enter a parse tree produced by TyCParser#andExprTail.
    def enterAndExprTail(self, ctx:TyCParser.AndExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#andExprTail.
    def exitAndExprTail(self, ctx:TyCParser.AndExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#equalExpr.
    def enterEqualExpr(self, ctx:TyCParser.EqualExprContext):
        pass

    # Exit a parse tree produced by TyCParser#equalExpr.
    def exitEqualExpr(self, ctx:TyCParser.EqualExprContext):
        pass


    # Enter a parse tree produced by TyCParser#equalExprTail.
    def enterEqualExprTail(self, ctx:TyCParser.EqualExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#equalExprTail.
    def exitEqualExprTail(self, ctx:TyCParser.EqualExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#compareExpr.
    def enterCompareExpr(self, ctx:TyCParser.CompareExprContext):
        pass

    # Exit a parse tree produced by TyCParser#compareExpr.
    def exitCompareExpr(self, ctx:TyCParser.CompareExprContext):
        pass


    # Enter a parse tree produced by TyCParser#compareExprTail.
    def enterCompareExprTail(self, ctx:TyCParser.CompareExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#compareExprTail.
    def exitCompareExprTail(self, ctx:TyCParser.CompareExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#addExpr.
    def enterAddExpr(self, ctx:TyCParser.AddExprContext):
        pass

    # Exit a parse tree produced by TyCParser#addExpr.
    def exitAddExpr(self, ctx:TyCParser.AddExprContext):
        pass


    # Enter a parse tree produced by TyCParser#addExprTail.
    def enterAddExprTail(self, ctx:TyCParser.AddExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#addExprTail.
    def exitAddExprTail(self, ctx:TyCParser.AddExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#mulExpr.
    def enterMulExpr(self, ctx:TyCParser.MulExprContext):
        pass

    # Exit a parse tree produced by TyCParser#mulExpr.
    def exitMulExpr(self, ctx:TyCParser.MulExprContext):
        pass


    # Enter a parse tree produced by TyCParser#mulExprTail.
    def enterMulExprTail(self, ctx:TyCParser.MulExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#mulExprTail.
    def exitMulExprTail(self, ctx:TyCParser.MulExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#unaryExpr.
    def enterUnaryExpr(self, ctx:TyCParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by TyCParser#unaryExpr.
    def exitUnaryExpr(self, ctx:TyCParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by TyCParser#unaryOp.
    def enterUnaryOp(self, ctx:TyCParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by TyCParser#unaryOp.
    def exitUnaryOp(self, ctx:TyCParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by TyCParser#postfixExpr.
    def enterPostfixExpr(self, ctx:TyCParser.PostfixExprContext):
        pass

    # Exit a parse tree produced by TyCParser#postfixExpr.
    def exitPostfixExpr(self, ctx:TyCParser.PostfixExprContext):
        pass


    # Enter a parse tree produced by TyCParser#postfixExprTail.
    def enterPostfixExprTail(self, ctx:TyCParser.PostfixExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#postfixExprTail.
    def exitPostfixExprTail(self, ctx:TyCParser.PostfixExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#postfixOp.
    def enterPostfixOp(self, ctx:TyCParser.PostfixOpContext):
        pass

    # Exit a parse tree produced by TyCParser#postfixOp.
    def exitPostfixOp(self, ctx:TyCParser.PostfixOpContext):
        pass


    # Enter a parse tree produced by TyCParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:TyCParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by TyCParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:TyCParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by TyCParser#structInit.
    def enterStructInit(self, ctx:TyCParser.StructInitContext):
        pass

    # Exit a parse tree produced by TyCParser#structInit.
    def exitStructInit(self, ctx:TyCParser.StructInitContext):
        pass


    # Enter a parse tree produced by TyCParser#structInitList.
    def enterStructInitList(self, ctx:TyCParser.StructInitListContext):
        pass

    # Exit a parse tree produced by TyCParser#structInitList.
    def exitStructInitList(self, ctx:TyCParser.StructInitListContext):
        pass


    # Enter a parse tree produced by TyCParser#structInitListSub.
    def enterStructInitListSub(self, ctx:TyCParser.StructInitListSubContext):
        pass

    # Exit a parse tree produced by TyCParser#structInitListSub.
    def exitStructInitListSub(self, ctx:TyCParser.StructInitListSubContext):
        pass


    # Enter a parse tree produced by TyCParser#argList.
    def enterArgList(self, ctx:TyCParser.ArgListContext):
        pass

    # Exit a parse tree produced by TyCParser#argList.
    def exitArgList(self, ctx:TyCParser.ArgListContext):
        pass


    # Enter a parse tree produced by TyCParser#argListSub.
    def enterArgListSub(self, ctx:TyCParser.ArgListSubContext):
        pass

    # Exit a parse tree produced by TyCParser#argListSub.
    def exitArgListSub(self, ctx:TyCParser.ArgListSubContext):
        pass



del TyCParser