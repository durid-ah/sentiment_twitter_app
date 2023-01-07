SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[trend_daily_aggregate](
	[id] [char](32) NOT NULL,
	[name] [nvarchar](500) NOT NULL,
	[tweet_volume] [int] NULL,
	[label_1] [int] NOT NULL,
	[label_2] [int] NOT NULL,
	[label_3] [int] NOT NULL,
	[label_4] [int] NOT NULL,
	[label_5] [int] NOT NULL,
	[total_count] [int] NOT NULL,
	[date] [datetime2](7) NOT NULL,
	[trend_id] [char](32) NOT NULL
) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
ALTER TABLE [dbo].[trend_daily_aggregate] ADD PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[trend_daily_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_daily_aggregate_trend_id_3f31366a_fk_twitter_trend_id] FOREIGN KEY([trend_id])
REFERENCES [dbo].[twitter_trend] ([id])
GO
ALTER TABLE [dbo].[trend_daily_aggregate] CHECK CONSTRAINT [trend_daily_aggregate_trend_id_3f31366a_fk_twitter_trend_id]
GO
ALTER TABLE [dbo].[trend_daily_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_daily_aggregate_label_1_989b537c_check] CHECK  (([label_1]>=(0)))
GO
ALTER TABLE [dbo].[trend_daily_aggregate] CHECK CONSTRAINT [trend_daily_aggregate_label_1_989b537c_check]
GO
ALTER TABLE [dbo].[trend_daily_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_daily_aggregate_label_2_59948ae6_check] CHECK  (([label_2]>=(0)))
GO
ALTER TABLE [dbo].[trend_daily_aggregate] CHECK CONSTRAINT [trend_daily_aggregate_label_2_59948ae6_check]
GO
ALTER TABLE [dbo].[trend_daily_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_daily_aggregate_label_3_5db7ad0e_check] CHECK  (([label_3]>=(0)))
GO
ALTER TABLE [dbo].[trend_daily_aggregate] CHECK CONSTRAINT [trend_daily_aggregate_label_3_5db7ad0e_check]
GO
ALTER TABLE [dbo].[trend_daily_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_daily_aggregate_label_4_99420b7e_check] CHECK  (([label_4]>=(0)))
GO
ALTER TABLE [dbo].[trend_daily_aggregate] CHECK CONSTRAINT [trend_daily_aggregate_label_4_99420b7e_check]
GO
ALTER TABLE [dbo].[trend_daily_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_daily_aggregate_label_5_6a9292b6_check] CHECK  (([label_5]>=(0)))
GO
ALTER TABLE [dbo].[trend_daily_aggregate] CHECK CONSTRAINT [trend_daily_aggregate_label_5_6a9292b6_check]
GO
ALTER TABLE [dbo].[trend_daily_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_daily_aggregate_total_count_90f1e005_check] CHECK  (([total_count]>=(0)))
GO
ALTER TABLE [dbo].[trend_daily_aggregate] CHECK CONSTRAINT [trend_daily_aggregate_total_count_90f1e005_check]
GO
ALTER TABLE [dbo].[trend_daily_aggregate]  WITH CHECK ADD  CONSTRAINT [trend_daily_aggregate_tweet_volume_b46ada38_check] CHECK  (([tweet_volume]>=(0)))
GO
ALTER TABLE [dbo].[trend_daily_aggregate] CHECK CONSTRAINT [trend_daily_aggregate_tweet_volume_b46ada38_check]
GO
