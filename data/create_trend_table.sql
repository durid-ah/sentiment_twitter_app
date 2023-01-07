SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[twitter_trend](
	[id] [char](32) NOT NULL,
	[name] [nvarchar](500) NOT NULL,
	[url] [nvarchar](200) NOT NULL,
	[created_date] [datetime2](7) NOT NULL,
	[last_used_date] [datetime2](7) NOT NULL,
	[query] [nvarchar](500) NOT NULL,
	[tweet_volume] [int] NULL
) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
ALTER TABLE [dbo].[twitter_trend] ADD PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[twitter_trend]  WITH CHECK ADD CHECK  (([tweet_volume]>=(0)))
GO
