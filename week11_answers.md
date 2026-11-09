# Week 11 answers

## Excercise 1
1. The message the customer never saw:
2. How many times the customer has spoken:
3. Can the model tell that the last reply came from the order tool? Why does that matter?
4. The customer now types "Thanks". How many messages are sent on the next call?

1. The message the customer never saw: the system message, which holds the instructions
2. How many times the customer has spoken: twice
3. No, In the history every reply has the role assistant, whether a rule, a tool, or the model wrote it. The model reads the whole history, so it can copy the pattern of an earlier tool answer and state something the tool never said. 
4. Six: the five messages above plus the new user message

Thank you for bringing that to our attention. As a support assistant, I don't close the store myself, but based on the most recent information, Bayside Outfitters now closes at 11 pm.
A reply like this could cost a real shop because the bot is giving out false information. This would cost a shop to seem not reliable and put their customers in bad positions. The bots are not reliable and should only be able to say facts that cannot be changed by the messanger. 