SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[trend_aggregate](
	[id] [char](32) NOT NULL,
	[name] [nvarchar](500) NOT NULL,
	[label_1] [int] NOT NULL,
	[label_2] [int] NOT NULL,
	[label_3] [int] NOT NULL,
	[label_4] [int] NOT NULL,
	[label_5] [int] NOT NULL,
	[total_count] [int] NOT NULL,
	[trend_id] [char](32) NOT NULL
) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
ALTER TABLE [dbo].[trend_aggregate] ADD PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[trend_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_aggregate_trend_id_bdf11319_fk_twitter_trend_id] FOREIGN KEY([trend_id])
REFERENCES [dbo].[twitter_trend] ([id])
GO
ALTER TABLE [dbo].[trend_aggregate] CHECK CONSTRAINT [trend_aggregate_trend_id_bdf11319_fk_twitter_trend_id]
GO
ALTER TABLE [dbo].[trend_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_aggregate_label_1_b45f874a_check] CHECK  (([label_1]>=(0)))
GO
ALTER TABLE [dbo].[trend_aggregate] CHECK CONSTRAINT [trend_aggregate_label_1_b45f874a_check]
GO
ALTER TABLE [dbo].[trend_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_aggregate_label_2_f69aeaae_check] CHECK  (([label_2]>=(0)))
GO
ALTER TABLE [dbo].[trend_aggregate] CHECK CONSTRAINT [trend_aggregate_label_2_f69aeaae_check]
GO
ALTER TABLE [dbo].[trend_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_aggregate_label_3_455cb131_check] CHECK  (([label_3]>=(0)))
GO
ALTER TABLE [dbo].[trend_aggregate] CHECK CONSTRAINT [trend_aggregate_label_3_455cb131_check]
GO
ALTER TABLE [dbo].[trend_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_aggregate_label_4_20a6b6e7_check] CHECK  (([label_4]>=(0)))
GO
ALTER TABLE [dbo].[trend_aggregate] CHECK CONSTRAINT [trend_aggregate_label_4_20a6b6e7_check]
GO
ALTER TABLE [dbo].[trend_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_aggregate_label_5_90f0a3b2_check] CHECK  (([label_5]>=(0)))
GO
ALTER TABLE [dbo].[trend_aggregate] CHECK CONSTRAINT [trend_aggregate_label_5_90f0a3b2_check]
GO
ALTER TABLE [dbo].[trend_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_aggregate_total_count_88ca8edc_check] CHECK  (([total_count]>=(0)))
GO
ALTER TABLE [dbo].[trend_aggregate] CHECK CONSTRAINT [trend_aggregate_total_count_88ca8edc_check]
GO
