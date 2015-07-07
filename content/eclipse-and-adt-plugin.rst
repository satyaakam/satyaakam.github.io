Eclipse and ADT plugin
######################
:date: 2011-10-21 21:57
:author: satya
:category: Android, Eclipse, FOSS
:slug: eclipse-and-adt-plugin
:status: published

Eclipse 3.6.2 which come with Fedora does play well with `ADT
plugin <http://developer.android.com/sdk/eclipse-adt.html#installing>`__
, it gives the following errors

| Cannot complete the install because one or more required items could
  not be found.
|  Software being installed: Android Development Tools
  0.9.9.v201009221407-60953 (com.android.ide.eclipse.adt.feature.group
  0.9.9.v201009221407-60953)
|  Missing requirement: Android Development Tools
  0.9.9.v201009221407-60953 (com.android.ide.eclipse.adt.feature.group
  0.9.9.v201009221407-60953) requires 'org.eclipse.wst.sse.core 0.0.0'
  but it could not be found

you can get over it by following these steps

| Select Help > Install New Software...
|  Click the link for Available Software Sites.
|  Ensure there is an update site named Helios. If this is not present,
  click Add... and enter http://download.eclipse.org/releases/helios for
  the Location.
|  Now go through the installation steps; Eclipse should download and
  install the plugin's dependencies.
