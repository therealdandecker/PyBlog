Title: SQL Adventures
Date: 2020-04-04 21:40
Tags: Python, Blog, SQL
Category: Data
Author: Dan

Continuing to grind things out in the midst of the COVID-19 epidemic.  The web scraping projects from the prior weekend and building a static site have been good distractions.

I played around with Hugo (Go(lang)) yesterday a bit but on the advice of my wife decided to stick with one project at a time.

I did stumble on something interesting today- reading an article on Medium.com about Jinja2.

Jinja2 has support for dynamic SQL with Python, which is something I could have used sorely yesterday.  Short version - our team needed to execute several loops of SQL simulteneously across 10 servers, which was really a painful experience.  Thanks to the support of the team I work with we got it done, but it was not without its issues.  Needless to say, something like Jinja2 and ODBC probably would have been more pragmatic than a dynamic for loop in SQL.

I struggle a little with if/when to leverage Python within SQL beyond the ETL jobs I run today; I find something like SSIS clunky and cumbersome, while other tools are simply too expensive for what we need.  Scheduled Python jobs are how we roll, which are actually much better at ingesting things like flat files anyway than SQL will be.

