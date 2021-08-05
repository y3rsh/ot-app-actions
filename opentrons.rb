cask "opentrons" do
    name "opentrons"
    desc "opentrons app"
    version "4.5.0"
    homepage "https://s3.amazonaws.com"
    url "https://s3.amazonaws.com/opentrons-app/builds/Opentrons-v4.5.0-mac-b12575.dmg"
    sha256 :no_check
    app "Opentrons.app"
end