# Meeting transcript — LogRocket testing (Ema + Aashay)

**Date:** 2026-11-05  
**Topic:** LogRocket on Unqork, what gets recorded, first-day exploration  
**Participants:** Aashay Bhargava, Swapnil Patil, Emanuel Pedraza  
**Recording:** [Teams meeting recap (Ema + Aashay about Testing LogRocket)](https://teams.microsoft.com/l/meetingrecap?driveId=b%21zFIgiSK86UyXYOvr-VBeXn9OlEbFLA5KrBpdOn2kYzPSxcBdQhSkRJrptucHS1Dd&driveItemId=01DUICRDRARMVLRPET3FALRZUP3NXKS5GR&sitePath=https%3A%2F%2Fascensus0-my.sharepoint.com%2F%3Av%3A%2Fg%2Fpersonal%2Femanuel_pedraza_ascensus_com%2FIQAgiyq4vJPZQLjmj9tuqXTRARwenDEDnThCJlcn9XNdChA&fileUrl=https%3A%2F%2Fascensus0-my.sharepoint.com%2Fpersonal%2Femanuel_pedraza_ascensus_com%2FDocuments%2FRecordings%2FEma+%2B+Aashay+about+Testing+LogRocket-20261105_141113-Meeting+Recording.mp4%3Fweb%3D1&iCalUid=040000008200E00074C5B7101A82E0080000000091178922326DDD01000000000000000010000000A8450C1195A77A498DB7CFF37F2C31F0&threadId=19%3Ameeting_NmI2MmJmNjAtYTJhZS00ODZiLWEyYTgtZGE5ZDY0ZjQyMWMy%40thread.v2&organizerId=a4cddb8c-1088-4ffe-8fa8-0035a671d6a3&tenantId=1d3bed01-6d09-498e-ab05-f1e2fdb1b138&callId=a7b0d69a-f366-4d2c-9be2-3660e783a850&threadType=Meeting&meetingType=Scheduled&subType=RecapSharingLink_RecapCore&recapType=RecordingAndTranscript)

> Transcript as provided (speaker labels and timestamps kept). A segment about personal employment timing was removed from this repo copy.

---

**Aashay Bhargava** 0:03  
That what we are talking about, appreciate the technology, yes, appreciate the technology, and that's it. I'm, so we are not expecting anything from you right now on this one, but anyways, okay, so, yeah, but go ahead and record, I don't have any issues. That was not an excuse for not recording it.

**Swapnil Patil** 0:03  
Oh yeah, yeah, definitely, definitely man. Wherever I can help you guys, right? I'm there too.  
No, no worries, no worries at all. I can, I can speak.  
Thank you. Thank you.

**Aashay Bhargava** 0:23  
Yeah.

**Swapnil Patil** 0:26  
I just have the consent, you know.

**Aashay Bhargava** 0:28  
Like, Sso.  
So the thing is that currently Logrocket, this implementation, this talks about any application which is in Unqork environment and we have enabled Logrocket in QA and dev environment for Unqork. So it is reporting all these sessions, any user session that is created.  
Will be reported to Logrocket, right? Whatever I am doing in the application that are on Unqork, that all will be reported to Logrocket. It will, in fact, record that session and keep that recording.  
There is some 30 days or something like the time period is there in which this will be recorded. After that, it will start posting it. So for example, if we see this one, so we can see all these recordings which are there for different users, right? So let's say if I click on this one, right?

**Aashay Bhargava** 29:45  
For the starting, we can start with one of them, because code-wise, we are not actually writing in each of these flows. So it's being updated in the flow, which is common to all of them, right? So there is no specific reason why it should work in one of them and not in other.

**Swapnil Patil** 29:56  
Oh, it's a common code base. OK, yeah.

**Aashay Bhargava** 30:04  
But the L.  
Yes.  
Right.  
Ide.

**Swapnil Patil** 30:12  
I get it, yeah, yeah, I get it, OK.

**Aashay Bhargava** 30:14  
But it would be great if you can just randomly try a different one different time, right?

**Swapnil Patil** 30:17  
Yeah, yeah, yeah. So what I can do, right? I can first of all understand how this whole thing works. Then I can work on how to automate it, right? So automation can be much more easier that we can run for multiple one of them rather than doing manual. But I can explore that later as long as I understand the business and all, right? So then that can be done, yes.

**Aashay Bhargava** 30:33  
Right.

**Swapnil Patil** 30:37  
Definitely, but.

**Aashay Bhargava** 30:37  
And maybe you can start playing with this QA links. It's fine. You cannot do any damage as such over there. So you can just play with them to see which screen is capturing what and what are the various options that are.

**Swapnil Patil** 30:41  
Okay.  
Okay, these ones right, so yeah.  
Yeah.  
Yeah, yeah. Okay.  
I can do that, yes.

**Aashay Bhargava** 30:56  
Okay, I think I think it's good for the first day, the ice breaking.

**Swapnil Patil** 31:01  
I know, I know. You don't want me to scare, get scared. Yes, yes, yes.

**Aashay Bhargava** 31:05  
Will follow with four sessions like this.

**Emanuel Pedraza** 31:05  
Quick question.

**Emanuel Pedraza** 31:07  
So, Neil, as a quick question, when will be your official first day? Because Gregory said, add him everywhere. And I said, well, I will add him, but when is the official day? And when I saw you on the call, because I said, hey, Paul, Gregory said, add him everywhere. And he said, don't add him yet. And I said, well, I already add him.

**Swapnil Patil** 31:26  
Yeah.

**Emanuel Pedraza** 31:26  
Shoot, I want you to prepare the team. So that's why he was like, okay, this is the stuff.

**Swapnil Patil** 31:31  
Let me tell you, okay? I'll give, so I'm confused about this, okay?

**Emanuel Pedraza** 31:34  
If you want to drop Aashay, sorry, it's just curiosity from my end. Aashay, if you want to go back to...

**Swapnil Patil** 31:38  
[Segment removed: personal employment timing discussion.]

**Aashay Bhargava** 31:46  
We need to stop recording now.

**Emanuel Pedraza** 31:48  
Ohh, yes.

**Aashay Bhargava** 31:50  
Okay.
