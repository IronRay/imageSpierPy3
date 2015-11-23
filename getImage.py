#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import urllib.request
import time

from bs4 import BeautifulSoup

baseUrl = 'http://www.socwall.com/wallpapers/page:'
# regularExpression = '<a class="." '
sourceTitle = 'http://www.socwall.com/'

basePath = '/Users/Ray/Developer/ProgrammeExercise/Python/imageSpiderPy3/originData/image'
fileName = '.jpg'

i = 0

startNumber = 1
EnderNumber = 662

ISOTIMEFORMAT = '%Y - %m - %d %X'


# Print local time
def localTime():
    localTime = time.strftime(ISOTIMEFORMAT, time.localtime())
    return localTime


# Get Data
def getData(url):
    req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    )

    originPage = urllib.request.urlopen(req)
    data = originPage.read()
    # data = page.decode('UTF-8')

    return data


# Get target url
def getTargetUrl(sourceUrl, className):
    originUrl = BeautifulSoup(getData(sourceUrl), 'lxml')
    targetUrl = originUrl.find_all('a', className)
    return targetUrl


# Save Image
def saveImage(data, basePath, pageIndex, imageID, fileType):
    path = basePath + '_' + str(pageIndex) + '_' + str(imageID) + fileType
    imageName = 'image_' + str(pageIndex) + '_' + str(imageID) + fileType
    # print(path)
    # print('---')
    with open(path, 'wb') as file:
        file.write(data)
        file.close()
    print('File: ' + imageName + ' saved successfully!')


def getImageData(downloadLink, pageIndex, imageID):
    iamgeByte = getData(downloadLink)

    basePath = '/Users/Ray/Developer/ProgrammeExercise/Python/imageSpiderPy3/originData/image'
    fileType = '.jpg'

    print('Get Image Data Successfully!')
    saveImage(iamgeByte, basePath, pageIndex, imageID, fileType)


for i in range(startNumber, EnderNumber + 1):
    sourceUrl = baseUrl + str(i)
    pageIndex = i

    print(localTime())
    print(sourceUrl)
    print('Page:' + str(pageIndex) + ' downloading!')
    imageID = 0

    for link in getTargetUrl(sourceUrl, 'image'):
        imageID += 1
        imageViewLink = link.get('href')
        # print(imageViewLink)
        imageViewLink = sourceTitle + imageViewLink

        print(localTime() + ' Image:' + str(imageID) + ' downloading!')
        print(imageViewLink)

        for link in getTargetUrl(imageViewLink, 'download'):
            downloadLink = link.get('href')
            # print(downloadLink)
            downloadLink = sourceTitle + downloadLink
            print(downloadLink)
            try:
                getImageData(downloadLink, pageIndex, imageID)
                print('------')

            except:
                print("Spider don't work by some unkonw error.")
                print('------')

        time.sleep(3)

    print('Page:' + pageIndex + ' download successfully')
    print('------')
