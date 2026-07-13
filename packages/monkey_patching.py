import package1.m1


def patch():
    print("this is a patch function")

package1.m1.hello=patch

package1.m1.hello()