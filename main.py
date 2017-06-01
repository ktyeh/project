# -*-coding=utf8-*-
'''Project DocString
This is an example docstring. I have nothing to say here.
'''
import env
from logger import Logger
from todo import Client, OnMessageError, ServiceNameError
from options import options
from conf import get_conf

# import service-wise packages from lib
from lib import Project

service_name = 'project'

service_home = env.get_env(service_name)
opts = options(service_home)
logger = Logger(service_name, service_home)
client = Client(service_name)
conf = get_conf(service_home)


def on_message(_from, message):
    '''Deal with new message from to-do list'''
    logger.debug('on_message: %s, %s' % (_from, message))
    print '%s:  %s\n' % (service_from, message)
    client.publish('messager', 'hi, im %s' % _name)


def main():
    logger.info('main start')
    project = Project(opts.example)

    logger.debug('project.greeting()')
    project.greeting()

    #print conf
    
    logger.debug('set client.on_message')
    client.on_message = on_message

    try:
        logger.info('client.loop_forever')
        client.loop_forever()
    except KeyboardInterrupt:
        logger.info('exit(0)')
    except OnMessageError as e:
        print 'OnMessageError: %s' % str(e.message)
        logger.error('OnMessageError: %s' % str(e.message))
        logger.error('exit(2)')
    except ServiceNameError as e:
        print 'ServiceNameError: %s' % str(e.message)
        logger.error('ServiceNameError: %s' % str(e.message))
        logger.error('exit(2)')


if __name__ == '__main__':
    main()
