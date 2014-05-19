Testing
=======

Ssshh! is extensively tested. Developers run the unittest suite
continuously. Travis-CI runs both the unittest and integration test
suites.


Unittests
---------

Ssshh! is written test first. Unittests are deliberately kept fast. Mocks
are used sparingly, helping resist tight coupling to particular
implementations; behaviours are tested not implementations.


Integration Tests
-----------------

Integration tests are treated as a deliverable artifact; they are
polished to the same level as the application itself. They serve as the
definitive reference of application behaviour. This is especially useful
to API users.

