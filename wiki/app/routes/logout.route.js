function route_logout(config) {
  return function (req, res) {
    req.session.loggedIn = false;
    req.session.username = null;
    res.redirect(`${config.base_url}/login`);
  };
}

// Exports
module.exports = route_logout;
