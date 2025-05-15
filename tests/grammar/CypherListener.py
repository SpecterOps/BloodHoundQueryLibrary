# Generated from Cypher.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .CypherParser import CypherParser
else:
    from CypherParser import CypherParser


# This class defines a complete listener for a parse tree produced by CypherParser.
class CypherListener(ParseTreeListener):

    # Enter a parse tree produced by CypherParser#oC_Cypher.
    def enterOC_Cypher(self, ctx: CypherParser.OC_CypherContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Cypher.
    def exitOC_Cypher(self, ctx: CypherParser.OC_CypherContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_QueryOptions.
    def enterOC_QueryOptions(self, ctx: CypherParser.OC_QueryOptionsContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_QueryOptions.
    def exitOC_QueryOptions(self, ctx: CypherParser.OC_QueryOptionsContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_AnyCypherOption.
    def enterOC_AnyCypherOption(self, ctx: CypherParser.OC_AnyCypherOptionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_AnyCypherOption.
    def exitOC_AnyCypherOption(self, ctx: CypherParser.OC_AnyCypherOptionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_CypherOption.
    def enterOC_CypherOption(self, ctx: CypherParser.OC_CypherOptionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_CypherOption.
    def exitOC_CypherOption(self, ctx: CypherParser.OC_CypherOptionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_VersionNumber.
    def enterOC_VersionNumber(self, ctx: CypherParser.OC_VersionNumberContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_VersionNumber.
    def exitOC_VersionNumber(self, ctx: CypherParser.OC_VersionNumberContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Explain.
    def enterOC_Explain(self, ctx: CypherParser.OC_ExplainContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Explain.
    def exitOC_Explain(self, ctx: CypherParser.OC_ExplainContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Profile.
    def enterOC_Profile(self, ctx: CypherParser.OC_ProfileContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Profile.
    def exitOC_Profile(self, ctx: CypherParser.OC_ProfileContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ConfigurationOption.
    def enterOC_ConfigurationOption(
        self, ctx: CypherParser.OC_ConfigurationOptionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ConfigurationOption.
    def exitOC_ConfigurationOption(
        self, ctx: CypherParser.OC_ConfigurationOptionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_Statement.
    def enterOC_Statement(self, ctx: CypherParser.OC_StatementContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Statement.
    def exitOC_Statement(self, ctx: CypherParser.OC_StatementContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Query.
    def enterOC_Query(self, ctx: CypherParser.OC_QueryContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Query.
    def exitOC_Query(self, ctx: CypherParser.OC_QueryContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_RegularQuery.
    def enterOC_RegularQuery(self, ctx: CypherParser.OC_RegularQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_RegularQuery.
    def exitOC_RegularQuery(self, ctx: CypherParser.OC_RegularQueryContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_BulkImportQuery.
    def enterOC_BulkImportQuery(self, ctx: CypherParser.OC_BulkImportQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_BulkImportQuery.
    def exitOC_BulkImportQuery(self, ctx: CypherParser.OC_BulkImportQueryContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_PeriodicCommitHint.
    def enterOC_PeriodicCommitHint(
        self, ctx: CypherParser.OC_PeriodicCommitHintContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_PeriodicCommitHint.
    def exitOC_PeriodicCommitHint(self, ctx: CypherParser.OC_PeriodicCommitHintContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_LoadCSVQuery.
    def enterOC_LoadCSVQuery(self, ctx: CypherParser.OC_LoadCSVQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_LoadCSVQuery.
    def exitOC_LoadCSVQuery(self, ctx: CypherParser.OC_LoadCSVQueryContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Union.
    def enterOC_Union(self, ctx: CypherParser.OC_UnionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Union.
    def exitOC_Union(self, ctx: CypherParser.OC_UnionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_SingleQuery.
    def enterOC_SingleQuery(self, ctx: CypherParser.OC_SingleQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_SingleQuery.
    def exitOC_SingleQuery(self, ctx: CypherParser.OC_SingleQueryContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_SinglePartQuery.
    def enterOC_SinglePartQuery(self, ctx: CypherParser.OC_SinglePartQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_SinglePartQuery.
    def exitOC_SinglePartQuery(self, ctx: CypherParser.OC_SinglePartQueryContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_MultiPartQuery.
    def enterOC_MultiPartQuery(self, ctx: CypherParser.OC_MultiPartQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_MultiPartQuery.
    def exitOC_MultiPartQuery(self, ctx: CypherParser.OC_MultiPartQueryContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_UpdatingClause.
    def enterOC_UpdatingClause(self, ctx: CypherParser.OC_UpdatingClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_UpdatingClause.
    def exitOC_UpdatingClause(self, ctx: CypherParser.OC_UpdatingClauseContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ReadingClause.
    def enterOC_ReadingClause(self, ctx: CypherParser.OC_ReadingClauseContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_ReadingClause.
    def exitOC_ReadingClause(self, ctx: CypherParser.OC_ReadingClauseContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Command.
    def enterOC_Command(self, ctx: CypherParser.OC_CommandContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Command.
    def exitOC_Command(self, ctx: CypherParser.OC_CommandContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_CreateUniqueConstraint.
    def enterOC_CreateUniqueConstraint(
        self, ctx: CypherParser.OC_CreateUniqueConstraintContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_CreateUniqueConstraint.
    def exitOC_CreateUniqueConstraint(
        self, ctx: CypherParser.OC_CreateUniqueConstraintContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_CreateNodePropertyExistenceConstraint.
    def enterOC_CreateNodePropertyExistenceConstraint(
        self, ctx: CypherParser.OC_CreateNodePropertyExistenceConstraintContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_CreateNodePropertyExistenceConstraint.
    def exitOC_CreateNodePropertyExistenceConstraint(
        self, ctx: CypherParser.OC_CreateNodePropertyExistenceConstraintContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_CreateRelationshipPropertyExistenceConstraint.
    def enterOC_CreateRelationshipPropertyExistenceConstraint(
        self, ctx: CypherParser.OC_CreateRelationshipPropertyExistenceConstraintContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_CreateRelationshipPropertyExistenceConstraint.
    def exitOC_CreateRelationshipPropertyExistenceConstraint(
        self, ctx: CypherParser.OC_CreateRelationshipPropertyExistenceConstraintContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_CreateIndex.
    def enterOC_CreateIndex(self, ctx: CypherParser.OC_CreateIndexContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_CreateIndex.
    def exitOC_CreateIndex(self, ctx: CypherParser.OC_CreateIndexContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_DropUniqueConstraint.
    def enterOC_DropUniqueConstraint(
        self, ctx: CypherParser.OC_DropUniqueConstraintContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_DropUniqueConstraint.
    def exitOC_DropUniqueConstraint(
        self, ctx: CypherParser.OC_DropUniqueConstraintContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_DropNodePropertyExistenceConstraint.
    def enterOC_DropNodePropertyExistenceConstraint(
        self, ctx: CypherParser.OC_DropNodePropertyExistenceConstraintContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_DropNodePropertyExistenceConstraint.
    def exitOC_DropNodePropertyExistenceConstraint(
        self, ctx: CypherParser.OC_DropNodePropertyExistenceConstraintContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_DropRelationshipPropertyExistenceConstraint.
    def enterOC_DropRelationshipPropertyExistenceConstraint(
        self, ctx: CypherParser.OC_DropRelationshipPropertyExistenceConstraintContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_DropRelationshipPropertyExistenceConstraint.
    def exitOC_DropRelationshipPropertyExistenceConstraint(
        self, ctx: CypherParser.OC_DropRelationshipPropertyExistenceConstraintContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_DropIndex.
    def enterOC_DropIndex(self, ctx: CypherParser.OC_DropIndexContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_DropIndex.
    def exitOC_DropIndex(self, ctx: CypherParser.OC_DropIndexContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Index.
    def enterOC_Index(self, ctx: CypherParser.OC_IndexContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Index.
    def exitOC_Index(self, ctx: CypherParser.OC_IndexContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_UniqueConstraint.
    def enterOC_UniqueConstraint(self, ctx: CypherParser.OC_UniqueConstraintContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_UniqueConstraint.
    def exitOC_UniqueConstraint(self, ctx: CypherParser.OC_UniqueConstraintContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_NodePropertyExistenceConstraint.
    def enterOC_NodePropertyExistenceConstraint(
        self, ctx: CypherParser.OC_NodePropertyExistenceConstraintContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_NodePropertyExistenceConstraint.
    def exitOC_NodePropertyExistenceConstraint(
        self, ctx: CypherParser.OC_NodePropertyExistenceConstraintContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_RelationshipPropertyExistenceConstraint.
    def enterOC_RelationshipPropertyExistenceConstraint(
        self, ctx: CypherParser.OC_RelationshipPropertyExistenceConstraintContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_RelationshipPropertyExistenceConstraint.
    def exitOC_RelationshipPropertyExistenceConstraint(
        self, ctx: CypherParser.OC_RelationshipPropertyExistenceConstraintContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_RelationshipPatternSyntax.
    def enterOC_RelationshipPatternSyntax(
        self, ctx: CypherParser.OC_RelationshipPatternSyntaxContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_RelationshipPatternSyntax.
    def exitOC_RelationshipPatternSyntax(
        self, ctx: CypherParser.OC_RelationshipPatternSyntaxContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_LoadCSV.
    def enterOC_LoadCSV(self, ctx: CypherParser.OC_LoadCSVContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_LoadCSV.
    def exitOC_LoadCSV(self, ctx: CypherParser.OC_LoadCSVContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Match.
    def enterOC_Match(self, ctx: CypherParser.OC_MatchContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Match.
    def exitOC_Match(self, ctx: CypherParser.OC_MatchContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Unwind.
    def enterOC_Unwind(self, ctx: CypherParser.OC_UnwindContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Unwind.
    def exitOC_Unwind(self, ctx: CypherParser.OC_UnwindContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Merge.
    def enterOC_Merge(self, ctx: CypherParser.OC_MergeContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Merge.
    def exitOC_Merge(self, ctx: CypherParser.OC_MergeContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_MergeAction.
    def enterOC_MergeAction(self, ctx: CypherParser.OC_MergeActionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_MergeAction.
    def exitOC_MergeAction(self, ctx: CypherParser.OC_MergeActionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Create.
    def enterOC_Create(self, ctx: CypherParser.OC_CreateContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Create.
    def exitOC_Create(self, ctx: CypherParser.OC_CreateContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_CreateUnique.
    def enterOC_CreateUnique(self, ctx: CypherParser.OC_CreateUniqueContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_CreateUnique.
    def exitOC_CreateUnique(self, ctx: CypherParser.OC_CreateUniqueContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Set.
    def enterOC_Set(self, ctx: CypherParser.OC_SetContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Set.
    def exitOC_Set(self, ctx: CypherParser.OC_SetContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_SetItem.
    def enterOC_SetItem(self, ctx: CypherParser.OC_SetItemContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_SetItem.
    def exitOC_SetItem(self, ctx: CypherParser.OC_SetItemContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Delete.
    def enterOC_Delete(self, ctx: CypherParser.OC_DeleteContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Delete.
    def exitOC_Delete(self, ctx: CypherParser.OC_DeleteContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Remove.
    def enterOC_Remove(self, ctx: CypherParser.OC_RemoveContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Remove.
    def exitOC_Remove(self, ctx: CypherParser.OC_RemoveContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_RemoveItem.
    def enterOC_RemoveItem(self, ctx: CypherParser.OC_RemoveItemContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_RemoveItem.
    def exitOC_RemoveItem(self, ctx: CypherParser.OC_RemoveItemContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Foreach.
    def enterOC_Foreach(self, ctx: CypherParser.OC_ForeachContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Foreach.
    def exitOC_Foreach(self, ctx: CypherParser.OC_ForeachContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_InQueryCall.
    def enterOC_InQueryCall(self, ctx: CypherParser.OC_InQueryCallContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_InQueryCall.
    def exitOC_InQueryCall(self, ctx: CypherParser.OC_InQueryCallContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_StandaloneCall.
    def enterOC_StandaloneCall(self, ctx: CypherParser.OC_StandaloneCallContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_StandaloneCall.
    def exitOC_StandaloneCall(self, ctx: CypherParser.OC_StandaloneCallContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_YieldItems.
    def enterOC_YieldItems(self, ctx: CypherParser.OC_YieldItemsContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_YieldItems.
    def exitOC_YieldItems(self, ctx: CypherParser.OC_YieldItemsContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_YieldItem.
    def enterOC_YieldItem(self, ctx: CypherParser.OC_YieldItemContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_YieldItem.
    def exitOC_YieldItem(self, ctx: CypherParser.OC_YieldItemContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_With.
    def enterOC_With(self, ctx: CypherParser.OC_WithContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_With.
    def exitOC_With(self, ctx: CypherParser.OC_WithContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Return.
    def enterOC_Return(self, ctx: CypherParser.OC_ReturnContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Return.
    def exitOC_Return(self, ctx: CypherParser.OC_ReturnContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ProjectionBody.
    def enterOC_ProjectionBody(self, ctx: CypherParser.OC_ProjectionBodyContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_ProjectionBody.
    def exitOC_ProjectionBody(self, ctx: CypherParser.OC_ProjectionBodyContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ProjectionItems.
    def enterOC_ProjectionItems(self, ctx: CypherParser.OC_ProjectionItemsContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_ProjectionItems.
    def exitOC_ProjectionItems(self, ctx: CypherParser.OC_ProjectionItemsContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ProjectionItem.
    def enterOC_ProjectionItem(self, ctx: CypherParser.OC_ProjectionItemContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_ProjectionItem.
    def exitOC_ProjectionItem(self, ctx: CypherParser.OC_ProjectionItemContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Order.
    def enterOC_Order(self, ctx: CypherParser.OC_OrderContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Order.
    def exitOC_Order(self, ctx: CypherParser.OC_OrderContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Skip.
    def enterOC_Skip(self, ctx: CypherParser.OC_SkipContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Skip.
    def exitOC_Skip(self, ctx: CypherParser.OC_SkipContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Limit.
    def enterOC_Limit(self, ctx: CypherParser.OC_LimitContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Limit.
    def exitOC_Limit(self, ctx: CypherParser.OC_LimitContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_SortItem.
    def enterOC_SortItem(self, ctx: CypherParser.OC_SortItemContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_SortItem.
    def exitOC_SortItem(self, ctx: CypherParser.OC_SortItemContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Hint.
    def enterOC_Hint(self, ctx: CypherParser.OC_HintContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Hint.
    def exitOC_Hint(self, ctx: CypherParser.OC_HintContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Start.
    def enterOC_Start(self, ctx: CypherParser.OC_StartContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Start.
    def exitOC_Start(self, ctx: CypherParser.OC_StartContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_StartPoint.
    def enterOC_StartPoint(self, ctx: CypherParser.OC_StartPointContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_StartPoint.
    def exitOC_StartPoint(self, ctx: CypherParser.OC_StartPointContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Lookup.
    def enterOC_Lookup(self, ctx: CypherParser.OC_LookupContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Lookup.
    def exitOC_Lookup(self, ctx: CypherParser.OC_LookupContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_NodeLookup.
    def enterOC_NodeLookup(self, ctx: CypherParser.OC_NodeLookupContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_NodeLookup.
    def exitOC_NodeLookup(self, ctx: CypherParser.OC_NodeLookupContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_RelationshipLookup.
    def enterOC_RelationshipLookup(
        self, ctx: CypherParser.OC_RelationshipLookupContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_RelationshipLookup.
    def exitOC_RelationshipLookup(self, ctx: CypherParser.OC_RelationshipLookupContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_IdentifiedIndexLookup.
    def enterOC_IdentifiedIndexLookup(
        self, ctx: CypherParser.OC_IdentifiedIndexLookupContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_IdentifiedIndexLookup.
    def exitOC_IdentifiedIndexLookup(
        self, ctx: CypherParser.OC_IdentifiedIndexLookupContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_IndexQuery.
    def enterOC_IndexQuery(self, ctx: CypherParser.OC_IndexQueryContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_IndexQuery.
    def exitOC_IndexQuery(self, ctx: CypherParser.OC_IndexQueryContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_IdLookup.
    def enterOC_IdLookup(self, ctx: CypherParser.OC_IdLookupContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_IdLookup.
    def exitOC_IdLookup(self, ctx: CypherParser.OC_IdLookupContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_LiteralIds.
    def enterOC_LiteralIds(self, ctx: CypherParser.OC_LiteralIdsContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_LiteralIds.
    def exitOC_LiteralIds(self, ctx: CypherParser.OC_LiteralIdsContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Where.
    def enterOC_Where(self, ctx: CypherParser.OC_WhereContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Where.
    def exitOC_Where(self, ctx: CypherParser.OC_WhereContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Pattern.
    def enterOC_Pattern(self, ctx: CypherParser.OC_PatternContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Pattern.
    def exitOC_Pattern(self, ctx: CypherParser.OC_PatternContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_PatternPart.
    def enterOC_PatternPart(self, ctx: CypherParser.OC_PatternPartContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_PatternPart.
    def exitOC_PatternPart(self, ctx: CypherParser.OC_PatternPartContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_AnonymousPatternPart.
    def enterOC_AnonymousPatternPart(
        self, ctx: CypherParser.OC_AnonymousPatternPartContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_AnonymousPatternPart.
    def exitOC_AnonymousPatternPart(
        self, ctx: CypherParser.OC_AnonymousPatternPartContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_ShortestPathPattern.
    def enterOC_ShortestPathPattern(
        self, ctx: CypherParser.OC_ShortestPathPatternContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ShortestPathPattern.
    def exitOC_ShortestPathPattern(
        self, ctx: CypherParser.OC_ShortestPathPatternContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_PatternElement.
    def enterOC_PatternElement(self, ctx: CypherParser.OC_PatternElementContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_PatternElement.
    def exitOC_PatternElement(self, ctx: CypherParser.OC_PatternElementContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_RelationshipsPattern.
    def enterOC_RelationshipsPattern(
        self, ctx: CypherParser.OC_RelationshipsPatternContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_RelationshipsPattern.
    def exitOC_RelationshipsPattern(
        self, ctx: CypherParser.OC_RelationshipsPatternContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_NodePattern.
    def enterOC_NodePattern(self, ctx: CypherParser.OC_NodePatternContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_NodePattern.
    def exitOC_NodePattern(self, ctx: CypherParser.OC_NodePatternContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_PatternElementChain.
    def enterOC_PatternElementChain(
        self, ctx: CypherParser.OC_PatternElementChainContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_PatternElementChain.
    def exitOC_PatternElementChain(
        self, ctx: CypherParser.OC_PatternElementChainContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_RelationshipPattern.
    def enterOC_RelationshipPattern(
        self, ctx: CypherParser.OC_RelationshipPatternContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_RelationshipPattern.
    def exitOC_RelationshipPattern(
        self, ctx: CypherParser.OC_RelationshipPatternContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_RelationshipDetail.
    def enterOC_RelationshipDetail(
        self, ctx: CypherParser.OC_RelationshipDetailContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_RelationshipDetail.
    def exitOC_RelationshipDetail(self, ctx: CypherParser.OC_RelationshipDetailContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Properties.
    def enterOC_Properties(self, ctx: CypherParser.OC_PropertiesContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Properties.
    def exitOC_Properties(self, ctx: CypherParser.OC_PropertiesContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_RelType.
    def enterOC_RelType(self, ctx: CypherParser.OC_RelTypeContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_RelType.
    def exitOC_RelType(self, ctx: CypherParser.OC_RelTypeContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_RelationshipTypes.
    def enterOC_RelationshipTypes(self, ctx: CypherParser.OC_RelationshipTypesContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_RelationshipTypes.
    def exitOC_RelationshipTypes(self, ctx: CypherParser.OC_RelationshipTypesContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_NodeLabels.
    def enterOC_NodeLabels(self, ctx: CypherParser.OC_NodeLabelsContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_NodeLabels.
    def exitOC_NodeLabels(self, ctx: CypherParser.OC_NodeLabelsContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_NodeLabel.
    def enterOC_NodeLabel(self, ctx: CypherParser.OC_NodeLabelContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_NodeLabel.
    def exitOC_NodeLabel(self, ctx: CypherParser.OC_NodeLabelContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_RangeLiteral.
    def enterOC_RangeLiteral(self, ctx: CypherParser.OC_RangeLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_RangeLiteral.
    def exitOC_RangeLiteral(self, ctx: CypherParser.OC_RangeLiteralContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_LabelName.
    def enterOC_LabelName(self, ctx: CypherParser.OC_LabelNameContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_LabelName.
    def exitOC_LabelName(self, ctx: CypherParser.OC_LabelNameContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_RelTypeName.
    def enterOC_RelTypeName(self, ctx: CypherParser.OC_RelTypeNameContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_RelTypeName.
    def exitOC_RelTypeName(self, ctx: CypherParser.OC_RelTypeNameContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_PropertyExpression.
    def enterOC_PropertyExpression(
        self, ctx: CypherParser.OC_PropertyExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_PropertyExpression.
    def exitOC_PropertyExpression(self, ctx: CypherParser.OC_PropertyExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Expression.
    def enterOC_Expression(self, ctx: CypherParser.OC_ExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Expression.
    def exitOC_Expression(self, ctx: CypherParser.OC_ExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_OrExpression.
    def enterOC_OrExpression(self, ctx: CypherParser.OC_OrExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_OrExpression.
    def exitOC_OrExpression(self, ctx: CypherParser.OC_OrExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_XorExpression.
    def enterOC_XorExpression(self, ctx: CypherParser.OC_XorExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_XorExpression.
    def exitOC_XorExpression(self, ctx: CypherParser.OC_XorExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_AndExpression.
    def enterOC_AndExpression(self, ctx: CypherParser.OC_AndExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_AndExpression.
    def exitOC_AndExpression(self, ctx: CypherParser.OC_AndExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_NotExpression.
    def enterOC_NotExpression(self, ctx: CypherParser.OC_NotExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_NotExpression.
    def exitOC_NotExpression(self, ctx: CypherParser.OC_NotExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ComparisonExpression.
    def enterOC_ComparisonExpression(
        self, ctx: CypherParser.OC_ComparisonExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ComparisonExpression.
    def exitOC_ComparisonExpression(
        self, ctx: CypherParser.OC_ComparisonExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_PartialComparisonExpression.
    def enterOC_PartialComparisonExpression(
        self, ctx: CypherParser.OC_PartialComparisonExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_PartialComparisonExpression.
    def exitOC_PartialComparisonExpression(
        self, ctx: CypherParser.OC_PartialComparisonExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_StringListNullPredicateExpression.
    def enterOC_StringListNullPredicateExpression(
        self, ctx: CypherParser.OC_StringListNullPredicateExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_StringListNullPredicateExpression.
    def exitOC_StringListNullPredicateExpression(
        self, ctx: CypherParser.OC_StringListNullPredicateExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_StringPredicateExpression.
    def enterOC_StringPredicateExpression(
        self, ctx: CypherParser.OC_StringPredicateExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_StringPredicateExpression.
    def exitOC_StringPredicateExpression(
        self, ctx: CypherParser.OC_StringPredicateExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_ListPredicateExpression.
    def enterOC_ListPredicateExpression(
        self, ctx: CypherParser.OC_ListPredicateExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ListPredicateExpression.
    def exitOC_ListPredicateExpression(
        self, ctx: CypherParser.OC_ListPredicateExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_NullPredicateExpression.
    def enterOC_NullPredicateExpression(
        self, ctx: CypherParser.OC_NullPredicateExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_NullPredicateExpression.
    def exitOC_NullPredicateExpression(
        self, ctx: CypherParser.OC_NullPredicateExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_RegularExpression.
    def enterOC_RegularExpression(self, ctx: CypherParser.OC_RegularExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_RegularExpression.
    def exitOC_RegularExpression(self, ctx: CypherParser.OC_RegularExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_AddOrSubtractExpression.
    def enterOC_AddOrSubtractExpression(
        self, ctx: CypherParser.OC_AddOrSubtractExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_AddOrSubtractExpression.
    def exitOC_AddOrSubtractExpression(
        self, ctx: CypherParser.OC_AddOrSubtractExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_MultiplyDivideModuloExpression.
    def enterOC_MultiplyDivideModuloExpression(
        self, ctx: CypherParser.OC_MultiplyDivideModuloExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_MultiplyDivideModuloExpression.
    def exitOC_MultiplyDivideModuloExpression(
        self, ctx: CypherParser.OC_MultiplyDivideModuloExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_PowerOfExpression.
    def enterOC_PowerOfExpression(self, ctx: CypherParser.OC_PowerOfExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_PowerOfExpression.
    def exitOC_PowerOfExpression(self, ctx: CypherParser.OC_PowerOfExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_UnaryAddOrSubtractExpression.
    def enterOC_UnaryAddOrSubtractExpression(
        self, ctx: CypherParser.OC_UnaryAddOrSubtractExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_UnaryAddOrSubtractExpression.
    def exitOC_UnaryAddOrSubtractExpression(
        self, ctx: CypherParser.OC_UnaryAddOrSubtractExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_NonArithmeticOperatorExpression.
    def enterOC_NonArithmeticOperatorExpression(
        self, ctx: CypherParser.OC_NonArithmeticOperatorExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_NonArithmeticOperatorExpression.
    def exitOC_NonArithmeticOperatorExpression(
        self, ctx: CypherParser.OC_NonArithmeticOperatorExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_ListOperatorExpression.
    def enterOC_ListOperatorExpression(
        self, ctx: CypherParser.OC_ListOperatorExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ListOperatorExpression.
    def exitOC_ListOperatorExpression(
        self, ctx: CypherParser.OC_ListOperatorExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_PropertyLookup.
    def enterOC_PropertyLookup(self, ctx: CypherParser.OC_PropertyLookupContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_PropertyLookup.
    def exitOC_PropertyLookup(self, ctx: CypherParser.OC_PropertyLookupContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Atom.
    def enterOC_Atom(self, ctx: CypherParser.OC_AtomContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Atom.
    def exitOC_Atom(self, ctx: CypherParser.OC_AtomContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_CaseExpression.
    def enterOC_CaseExpression(self, ctx: CypherParser.OC_CaseExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_CaseExpression.
    def exitOC_CaseExpression(self, ctx: CypherParser.OC_CaseExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_CaseAlternative.
    def enterOC_CaseAlternative(self, ctx: CypherParser.OC_CaseAlternativeContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_CaseAlternative.
    def exitOC_CaseAlternative(self, ctx: CypherParser.OC_CaseAlternativeContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ListComprehension.
    def enterOC_ListComprehension(self, ctx: CypherParser.OC_ListComprehensionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_ListComprehension.
    def exitOC_ListComprehension(self, ctx: CypherParser.OC_ListComprehensionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_PatternComprehension.
    def enterOC_PatternComprehension(
        self, ctx: CypherParser.OC_PatternComprehensionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_PatternComprehension.
    def exitOC_PatternComprehension(
        self, ctx: CypherParser.OC_PatternComprehensionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_LegacyListExpression.
    def enterOC_LegacyListExpression(
        self, ctx: CypherParser.OC_LegacyListExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_LegacyListExpression.
    def exitOC_LegacyListExpression(
        self, ctx: CypherParser.OC_LegacyListExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_Reduce.
    def enterOC_Reduce(self, ctx: CypherParser.OC_ReduceContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Reduce.
    def exitOC_Reduce(self, ctx: CypherParser.OC_ReduceContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Quantifier.
    def enterOC_Quantifier(self, ctx: CypherParser.OC_QuantifierContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Quantifier.
    def exitOC_Quantifier(self, ctx: CypherParser.OC_QuantifierContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_FilterExpression.
    def enterOC_FilterExpression(self, ctx: CypherParser.OC_FilterExpressionContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_FilterExpression.
    def exitOC_FilterExpression(self, ctx: CypherParser.OC_FilterExpressionContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_PatternPredicate.
    def enterOC_PatternPredicate(self, ctx: CypherParser.OC_PatternPredicateContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_PatternPredicate.
    def exitOC_PatternPredicate(self, ctx: CypherParser.OC_PatternPredicateContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ParenthesizedExpression.
    def enterOC_ParenthesizedExpression(
        self, ctx: CypherParser.OC_ParenthesizedExpressionContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ParenthesizedExpression.
    def exitOC_ParenthesizedExpression(
        self, ctx: CypherParser.OC_ParenthesizedExpressionContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_IdInColl.
    def enterOC_IdInColl(self, ctx: CypherParser.OC_IdInCollContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_IdInColl.
    def exitOC_IdInColl(self, ctx: CypherParser.OC_IdInCollContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_FunctionInvocation.
    def enterOC_FunctionInvocation(
        self, ctx: CypherParser.OC_FunctionInvocationContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_FunctionInvocation.
    def exitOC_FunctionInvocation(self, ctx: CypherParser.OC_FunctionInvocationContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_FunctionName.
    def enterOC_FunctionName(self, ctx: CypherParser.OC_FunctionNameContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_FunctionName.
    def exitOC_FunctionName(self, ctx: CypherParser.OC_FunctionNameContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ExistentialSubquery.
    def enterOC_ExistentialSubquery(
        self, ctx: CypherParser.OC_ExistentialSubqueryContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ExistentialSubquery.
    def exitOC_ExistentialSubquery(
        self, ctx: CypherParser.OC_ExistentialSubqueryContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_ExplicitProcedureInvocation.
    def enterOC_ExplicitProcedureInvocation(
        self, ctx: CypherParser.OC_ExplicitProcedureInvocationContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ExplicitProcedureInvocation.
    def exitOC_ExplicitProcedureInvocation(
        self, ctx: CypherParser.OC_ExplicitProcedureInvocationContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_ImplicitProcedureInvocation.
    def enterOC_ImplicitProcedureInvocation(
        self, ctx: CypherParser.OC_ImplicitProcedureInvocationContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ImplicitProcedureInvocation.
    def exitOC_ImplicitProcedureInvocation(
        self, ctx: CypherParser.OC_ImplicitProcedureInvocationContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_ProcedureResultField.
    def enterOC_ProcedureResultField(
        self, ctx: CypherParser.OC_ProcedureResultFieldContext
    ):
        pass

    # Exit a parse tree produced by CypherParser#oC_ProcedureResultField.
    def exitOC_ProcedureResultField(
        self, ctx: CypherParser.OC_ProcedureResultFieldContext
    ):
        pass

    # Enter a parse tree produced by CypherParser#oC_ProcedureName.
    def enterOC_ProcedureName(self, ctx: CypherParser.OC_ProcedureNameContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_ProcedureName.
    def exitOC_ProcedureName(self, ctx: CypherParser.OC_ProcedureNameContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Namespace.
    def enterOC_Namespace(self, ctx: CypherParser.OC_NamespaceContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Namespace.
    def exitOC_Namespace(self, ctx: CypherParser.OC_NamespaceContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Variable.
    def enterOC_Variable(self, ctx: CypherParser.OC_VariableContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Variable.
    def exitOC_Variable(self, ctx: CypherParser.OC_VariableContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Literal.
    def enterOC_Literal(self, ctx: CypherParser.OC_LiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Literal.
    def exitOC_Literal(self, ctx: CypherParser.OC_LiteralContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_BooleanLiteral.
    def enterOC_BooleanLiteral(self, ctx: CypherParser.OC_BooleanLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_BooleanLiteral.
    def exitOC_BooleanLiteral(self, ctx: CypherParser.OC_BooleanLiteralContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_NumberLiteral.
    def enterOC_NumberLiteral(self, ctx: CypherParser.OC_NumberLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_NumberLiteral.
    def exitOC_NumberLiteral(self, ctx: CypherParser.OC_NumberLiteralContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_IntegerLiteral.
    def enterOC_IntegerLiteral(self, ctx: CypherParser.OC_IntegerLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_IntegerLiteral.
    def exitOC_IntegerLiteral(self, ctx: CypherParser.OC_IntegerLiteralContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_DoubleLiteral.
    def enterOC_DoubleLiteral(self, ctx: CypherParser.OC_DoubleLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_DoubleLiteral.
    def exitOC_DoubleLiteral(self, ctx: CypherParser.OC_DoubleLiteralContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ListLiteral.
    def enterOC_ListLiteral(self, ctx: CypherParser.OC_ListLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_ListLiteral.
    def exitOC_ListLiteral(self, ctx: CypherParser.OC_ListLiteralContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_MapLiteral.
    def enterOC_MapLiteral(self, ctx: CypherParser.OC_MapLiteralContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_MapLiteral.
    def exitOC_MapLiteral(self, ctx: CypherParser.OC_MapLiteralContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_PropertyKeyName.
    def enterOC_PropertyKeyName(self, ctx: CypherParser.OC_PropertyKeyNameContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_PropertyKeyName.
    def exitOC_PropertyKeyName(self, ctx: CypherParser.OC_PropertyKeyNameContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_LegacyParameter.
    def enterOC_LegacyParameter(self, ctx: CypherParser.OC_LegacyParameterContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_LegacyParameter.
    def exitOC_LegacyParameter(self, ctx: CypherParser.OC_LegacyParameterContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Parameter.
    def enterOC_Parameter(self, ctx: CypherParser.OC_ParameterContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Parameter.
    def exitOC_Parameter(self, ctx: CypherParser.OC_ParameterContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_SchemaName.
    def enterOC_SchemaName(self, ctx: CypherParser.OC_SchemaNameContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_SchemaName.
    def exitOC_SchemaName(self, ctx: CypherParser.OC_SchemaNameContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_ReservedWord.
    def enterOC_ReservedWord(self, ctx: CypherParser.OC_ReservedWordContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_ReservedWord.
    def exitOC_ReservedWord(self, ctx: CypherParser.OC_ReservedWordContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_SymbolicName.
    def enterOC_SymbolicName(self, ctx: CypherParser.OC_SymbolicNameContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_SymbolicName.
    def exitOC_SymbolicName(self, ctx: CypherParser.OC_SymbolicNameContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_LeftArrowHead.
    def enterOC_LeftArrowHead(self, ctx: CypherParser.OC_LeftArrowHeadContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_LeftArrowHead.
    def exitOC_LeftArrowHead(self, ctx: CypherParser.OC_LeftArrowHeadContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_RightArrowHead.
    def enterOC_RightArrowHead(self, ctx: CypherParser.OC_RightArrowHeadContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_RightArrowHead.
    def exitOC_RightArrowHead(self, ctx: CypherParser.OC_RightArrowHeadContext):
        pass

    # Enter a parse tree produced by CypherParser#oC_Dash.
    def enterOC_Dash(self, ctx: CypherParser.OC_DashContext):
        pass

    # Exit a parse tree produced by CypherParser#oC_Dash.
    def exitOC_Dash(self, ctx: CypherParser.OC_DashContext):
        pass


del CypherParser
