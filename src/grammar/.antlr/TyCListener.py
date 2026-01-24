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


    # Enter a parse tree produced by TyCParser#paramListNonEmpty.
    def enterParamListNonEmpty(self, ctx:TyCParser.ParamListNonEmptyContext):
        pass

    # Exit a parse tree produced by TyCParser#paramListNonEmpty.
    def exitParamListNonEmpty(self, ctx:TyCParser.ParamListNonEmptyContext):
        pass


    # Enter a parse tree produced by TyCParser#param.
    def enterParam(self, ctx:TyCParser.ParamContext):
        pass

    # Exit a parse tree produced by TyCParser#param.
    def exitParam(self, ctx:TyCParser.ParamContext):
        pass


    # Enter a parse tree produced by TyCParser#typeSpec.
    def enterTypeSpec(self, ctx:TyCParser.TypeSpecContext):
        pass

    # Exit a parse tree produced by TyCParser#typeSpec.
    def exitTypeSpec(self, ctx:TyCParser.TypeSpecContext):
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


    # Enter a parse tree produced by TyCParser#statementList.
    def enterStatementList(self, ctx:TyCParser.StatementListContext):
        pass

    # Exit a parse tree produced by TyCParser#statementList.
    def exitStatementList(self, ctx:TyCParser.StatementListContext):
        pass


    # Enter a parse tree produced by TyCParser#assignStmt.
    def enterAssignStmt(self, ctx:TyCParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#assignStmt.
    def exitAssignStmt(self, ctx:TyCParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#ifStmt.
    def enterIfStmt(self, ctx:TyCParser.IfStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#ifStmt.
    def exitIfStmt(self, ctx:TyCParser.IfStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#elseOpt.
    def enterElseOpt(self, ctx:TyCParser.ElseOptContext):
        pass

    # Exit a parse tree produced by TyCParser#elseOpt.
    def exitElseOpt(self, ctx:TyCParser.ElseOptContext):
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


    # Enter a parse tree produced by TyCParser#forCond.
    def enterForCond(self, ctx:TyCParser.ForCondContext):
        pass

    # Exit a parse tree produced by TyCParser#forCond.
    def exitForCond(self, ctx:TyCParser.ForCondContext):
        pass


    # Enter a parse tree produced by TyCParser#forUpdate.
    def enterForUpdate(self, ctx:TyCParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by TyCParser#forUpdate.
    def exitForUpdate(self, ctx:TyCParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by TyCParser#switchStmt.
    def enterSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        pass

    # Exit a parse tree produced by TyCParser#switchStmt.
    def exitSwitchStmt(self, ctx:TyCParser.SwitchStmtContext):
        pass


    # Enter a parse tree produced by TyCParser#caseClauseList.
    def enterCaseClauseList(self, ctx:TyCParser.CaseClauseListContext):
        pass

    # Exit a parse tree produced by TyCParser#caseClauseList.
    def exitCaseClauseList(self, ctx:TyCParser.CaseClauseListContext):
        pass


    # Enter a parse tree produced by TyCParser#caseClause.
    def enterCaseClause(self, ctx:TyCParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by TyCParser#caseClause.
    def exitCaseClause(self, ctx:TyCParser.CaseClauseContext):
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


    # Enter a parse tree produced by TyCParser#returnExpr.
    def enterReturnExpr(self, ctx:TyCParser.ReturnExprContext):
        pass

    # Exit a parse tree produced by TyCParser#returnExpr.
    def exitReturnExpr(self, ctx:TyCParser.ReturnExprContext):
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


    # Enter a parse tree produced by TyCParser#assignExprTail.
    def enterAssignExprTail(self, ctx:TyCParser.AssignExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#assignExprTail.
    def exitAssignExprTail(self, ctx:TyCParser.AssignExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#logicalOrExpr.
    def enterLogicalOrExpr(self, ctx:TyCParser.LogicalOrExprContext):
        pass

    # Exit a parse tree produced by TyCParser#logicalOrExpr.
    def exitLogicalOrExpr(self, ctx:TyCParser.LogicalOrExprContext):
        pass


    # Enter a parse tree produced by TyCParser#logicalOrExprTail.
    def enterLogicalOrExprTail(self, ctx:TyCParser.LogicalOrExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#logicalOrExprTail.
    def exitLogicalOrExprTail(self, ctx:TyCParser.LogicalOrExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#logicalAndExpr.
    def enterLogicalAndExpr(self, ctx:TyCParser.LogicalAndExprContext):
        pass

    # Exit a parse tree produced by TyCParser#logicalAndExpr.
    def exitLogicalAndExpr(self, ctx:TyCParser.LogicalAndExprContext):
        pass


    # Enter a parse tree produced by TyCParser#logicalAndExprTail.
    def enterLogicalAndExprTail(self, ctx:TyCParser.LogicalAndExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#logicalAndExprTail.
    def exitLogicalAndExprTail(self, ctx:TyCParser.LogicalAndExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#equalityExpr.
    def enterEqualityExpr(self, ctx:TyCParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by TyCParser#equalityExpr.
    def exitEqualityExpr(self, ctx:TyCParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by TyCParser#equalityExprTail.
    def enterEqualityExprTail(self, ctx:TyCParser.EqualityExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#equalityExprTail.
    def exitEqualityExprTail(self, ctx:TyCParser.EqualityExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#relationalExpr.
    def enterRelationalExpr(self, ctx:TyCParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by TyCParser#relationalExpr.
    def exitRelationalExpr(self, ctx:TyCParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by TyCParser#relationalExprTail.
    def enterRelationalExprTail(self, ctx:TyCParser.RelationalExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#relationalExprTail.
    def exitRelationalExprTail(self, ctx:TyCParser.RelationalExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:TyCParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by TyCParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:TyCParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by TyCParser#additiveExprTail.
    def enterAdditiveExprTail(self, ctx:TyCParser.AdditiveExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#additiveExprTail.
    def exitAdditiveExprTail(self, ctx:TyCParser.AdditiveExprTailContext):
        pass


    # Enter a parse tree produced by TyCParser#multiplicativeExpr.
    def enterMultiplicativeExpr(self, ctx:TyCParser.MultiplicativeExprContext):
        pass

    # Exit a parse tree produced by TyCParser#multiplicativeExpr.
    def exitMultiplicativeExpr(self, ctx:TyCParser.MultiplicativeExprContext):
        pass


    # Enter a parse tree produced by TyCParser#multiplicativeExprTail.
    def enterMultiplicativeExprTail(self, ctx:TyCParser.MultiplicativeExprTailContext):
        pass

    # Exit a parse tree produced by TyCParser#multiplicativeExprTail.
    def exitMultiplicativeExprTail(self, ctx:TyCParser.MultiplicativeExprTailContext):
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


    # Enter a parse tree produced by TyCParser#structInitListNonEmpty.
    def enterStructInitListNonEmpty(self, ctx:TyCParser.StructInitListNonEmptyContext):
        pass

    # Exit a parse tree produced by TyCParser#structInitListNonEmpty.
    def exitStructInitListNonEmpty(self, ctx:TyCParser.StructInitListNonEmptyContext):
        pass


    # Enter a parse tree produced by TyCParser#argList.
    def enterArgList(self, ctx:TyCParser.ArgListContext):
        pass

    # Exit a parse tree produced by TyCParser#argList.
    def exitArgList(self, ctx:TyCParser.ArgListContext):
        pass


    # Enter a parse tree produced by TyCParser#argListNonEmpty.
    def enterArgListNonEmpty(self, ctx:TyCParser.ArgListNonEmptyContext):
        pass

    # Exit a parse tree produced by TyCParser#argListNonEmpty.
    def exitArgListNonEmpty(self, ctx:TyCParser.ArgListNonEmptyContext):
        pass



del TyCParser