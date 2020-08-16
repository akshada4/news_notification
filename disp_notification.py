from news import stories
import notify2

def display_notification(news):
	notify2.init('notifier')
	n = notify2.Notification(None)
	n.update(news['title'],news['link'])
	n.show()
