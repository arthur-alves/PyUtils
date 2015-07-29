#!/usr/bin/env python
import gtk
import webkit
import gobject

gobject.threads_init()
win = gtk.Window()
# win.fullscreen()
sw = gtk.ScrolledWindow()
sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_NEVER)
bro = webkit.WebView()
# bro.props.settings.props.enable_default_context_menu = False
bro.open("http://www.google.com.br")
sw.add(bro)
win.add(sw)
win.show_all()
gtk.main()
