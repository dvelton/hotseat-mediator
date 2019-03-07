# hotseat-mediator

This program is designed to resolve legal disputes both simple and complex.
In real-world litigation, countless cases do not settle as fast as they 
can or should because of a straightforward rule of negotiation: parties' need 
to maintain bargaining position. 

For example, a Plaintiff who might be willing to accept $50,000 in full
resolution of his or her case is unlikely to indicate this willingness to a 
Defendant, knowing that Defendant will view this expressed $50,000 figure 
as a ceiling and simply negotiate down from there. The 
realities of negotiation require a Plaintiff aiming for $50,000 to 
begin by shooting much higher (for example, $100,000 or $150,000) in hopes of 
ending up at the desired amount. This method allows for Plaintiff to maintain
bargaining position. However, such artificially inflated amounts are roadblocks
to settlement. Perhaps Defendant would have been willing to pay $50,000, but 
to maintain his or her own bargaining position, Defendant must refrain from 
indicating this willingness in response to Plaintiff's inflated demands. Instead,
Defendant must stick to artificially low offers initially (such as $5,000 or $10,000).
In the above manner, parties inevitably end up at an impasse that can take months
or years and countless resources to break through. Even in a situation where 
both Plaintiff and Defendant would secretly be willing to settle a case for $50,000,
the case is not settled because the rules of negotiation encourage both Plaintiff 
and Defendant to maintain their respective bargaining positions. Plaintiff ends up
viewing Defendant as stubborn and unreasonable (because of Defendant's artificially low offers),
and Defendant views Plaintiff as wildly unrealistic (because of Plaintiff's artificially high demands).

This program creates information asymmetry between the parties and is 
a path toward breaking through the impasse. It is effectively a structured
negotiation that allows both Plaintiff and Defendant to indicate willingness
to settle at a certain number but WITHOUT the fear of loss of bargaining position! 

It does this as follows: Running through numbers in range(x, y, z), 
the program separately (via hotseat) asks Plaintiff and Defendant if each 
is willing to settle at a particular number. If both parties indicate "No" then
the program moves to the next number at z interval and asks the same question.
If both parties indicate "Yes" to a number then the program informs the parties that both
are willing to settle at the particular number. However, if one party indicates
"Yes" and the other party indicates "No" then the program moves on to the next
line but DOES NOT DISCLOSE to the "No" party that the other party had said "Yes."
In other words: a party can indicate "Yes" to a particular number without losing
bargaining position because if the other side says "No" to that number, the "No" side will
never know that there was even a "Yes" response to that number at all.

Finally, because of the nature of this program, parties have an incentive to be
honest with themselves. If they truly want to see if there is a number at which
both sides can settle, they will not posture and artificially inflate or lower 
their demands/offers out of fear of missing a possible window of "Yes" overlap 
and thus settlement.  

Thanks for reading this far. After practicing law and running a civil litigation
practice in Silicon Valley for nearly a decade, I started to study some programming
for fun. This is the first product. If you have any tips or improvements, 
please feel free to email me.
