# Workflow

1. User enters `/confluence creating a user`
2. Slack bot performs a query to Confluence and searches for the phrase "creating a user"
3. Top result is returned as a block
4. If more than one result is returned, a URL would be returned with a link to the other results. Or could we return top N results?
