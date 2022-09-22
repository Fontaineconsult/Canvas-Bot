import json
import os
from core_canvas_classes.canvas_page_wrapper import CanvasCourseWrapper
import datetime


def build_path(node):
    print("GETTING TIME")


    path_list = []
    def get_parent(node):
        print(node.__class__.__name__)
        path_list.append(node.__class__.__name__)
        print(node.root_node)
        if not node.root_node:
            get_parent(node.parent)

    path_list.append(node.title)
    get_parent(node.parent)
    print(path_list)


def main_dict(**items) -> dict:

    main_dict = {
        "content_type": items.get("content_type"),
        "course_title": items.get("course_title"),
        "course_id": items.get("course_id"),
        "course_url": items.get("course_url"),
        "content": list(),
        "count": items.get("count")
    }
    return main_dict


def audio_item_dict(**items):

    audio_item_dict = {

        "title": items.get("title"),
        "url": items.get("url"),
        "source_page_url": items.get("source_page_url"),
        "source_page_type": items.get("source_page_type"),
        "source_page_title": items.get("source_page_title"),
        "scan_date": datetime.datetime.now(),
        "is_hidden": items.get("is_hidden"),
        "content_type": items.get("title"),
        "mime_type": items.get("mime_type"),
        "order": items.get("order"),
        "downloadable": items.get("downloadable")

    }

    return audio_item_dict


def documents_item_dict(**items):

    document_item_dict = {

        "title": items.get("title"),
        "url": items.get("url"),
        "download_url": items.get("download_url"),
        "source_page_type": items.get("source_page_type"),
        "source_page_url": items.get("source_page_url"),
        "source_page_title": items.get("source_page_title"),
        "scan_date": datetime.datetime.now(),
        "is_hidden": items.get("is_hidden"),
        "content_type": items.get("content_type"),
        "mime_type": items.get("mime_type"),
        "order": items.get("order"),
        "downloadable": items.get("downloadable")

    }
    return document_item_dict


def video_item_dict(**items):

    video_item_dict = {

        "title": items.get("title"),
        "url": items.get("url"),
        "source_page_url": items.get("source_page_url"),
        "source_page_type": items.get("source_page_type"),
        "source_page_title": items.get("source_page_title"),
        "scan_date": datetime.datetime.now(),
        "is_hidden": items.get("is_hidden"),
        "content_type": items.get("content_type"),
        "mime_type": items.get("mime_type"),
        "order": items.get("order"),
        "downloadable": items.get("downloadable")

    }
    return video_item_dict


def image_item_dict(**items):

    image_item_dict = {

        "title": items.get("title"),
        "url": items.get("url"),
        "source_page_url": items.get("source_page_url"),
        "source_page_type": items.get("source_page_type"),
        "source_page_title": items.get("source_page_title"),
        "scan_date": datetime.datetime.now(),
        "is_hidden": items.get("is_hidden"),
        "content_type": items.get("content_type"),
        "alt_tag_present": items.get("alt_tag_present"),
        "order": items.get("order"),
        "downloadable": items.get("downloadable")

    }

    return image_item_dict

class ContentExtractor(CanvasCourseWrapper):

    def __init__(self, course_id, scraper, **kwargs):
        self.course_id = course_id
        CanvasCourseWrapper.__init__(self, course_id, scraper, **kwargs)


    def get_videos(self):
        videos = list()
        manifest = self.content_manifest.get_manifest()
        for item in manifest:
            if manifest[item][0].is_video:
                videos.append(manifest[item][0])
        return videos

    def get_documents(self):
        documents = list()
        manifest = self.content_manifest.get_manifest()
        for item in manifest:
            if manifest[item][0].is_document:
                documents.append(manifest[item][0])
        return documents

    def get_images(self):
        images = list()
        manifest = self.content_manifest.get_manifest()
        for item in manifest:
            if manifest[item][0].is_image:
                images.append(manifest[item][0])
        return images

    def get_audio(self):
        audio = list()
        manifest = self.content_manifest.get_manifest()
        for item in manifest:
            if manifest[item][0].is_audio:
                audio.append(manifest[item][0])
        return audio


    def get_videos_to_json(self, save=False):

        manifest = self.content_manifest.get_content()


        videos = main_dict(course_id=self.canvas_course_id,
                           course_title=None,
                           content_type="videos",
                           count=len(manifest),
                           course_url=self.course_page_url
                           )
        count = 0
        for item in manifest:

            if item.is_video:
                count += 1
                videos['content'].append(video_item_dict(
                    title=item.title,
                    url=item.url,
                    source_page_url=item.parent.url,
                    source_page_title=item.parent.title,
                    source_page_type=item.parent.__class__.__name__,
                    is_hidden=item.is_hidden,
                    content_type=item.__class__.__name__,
                    downloadable=item.downloadable,
                    mime_type=item.mime_type if item.downloadable is True else None,
                    order=item.order
                ))
        videos['count'] = count
        if save:
            return self._save_json_output(json.dumps(videos, indent=4, sort_keys=True, default=str))

        return videos

    def get_documents_to_json(self, save=False):

        manifest = self.content_manifest.get_content()
        documents = main_dict(course_id=self.canvas_course_id,
                              course_title=None,
                              content_type="documents",
                              count=len(manifest),
                              course_url=self.course_page_url
                              )
        count = 0
        for item in manifest:
            build_path(item)
            if item.is_document:
                count += 1
                documents['content'].append(documents_item_dict(
                    title=item.title,
                    url=item.url,
                    download_url=item.resource_location,
                    source_page_url=item.parent.url,
                    source_page_title=item.parent.title,
                    source_page_type=item.parent.__class__.__name__,
                    is_hidden=item.is_hidden,
                    content_type=item.__class__.__name__,
                    mime_type=item.mime_type,
                    downloadable=item.downloadable,
                    order=item.order
                ))
        documents['count'] = count
        if save:
            return self._save_json_output(json.dumps(documents, indent=4, sort_keys=True, default=str))

        return documents

    def get_images_to_json(self, save=False):
        manifest = self.content_manifest.get_content()
        images = main_dict(course_id=self.canvas_course_id,
                              course_title=None,
                              content_type="images",
                              count=len(manifest),
                              course_url=self.course_page_url
                              )
        count = 0
        for item in manifest:
            if item.is_image:
                count += 1
                images['content'].append(image_item_dict(
                    title=item.title,
                    url=item.url,
                    source_page_url=item.parent.url,
                    source_page_title=item.parent.title,
                    source_page_type=item.parent.__class__.__name__,
                    is_hidden=item.is_hidden,
                    content_type=item.__class__.__name__,
                    mime_type=item.mime_type,
                    alt_tag_present=item.alt_tag,
                    downloadable=item.downloadable,
                    order=item.order
                ))
        images['count'] = count
        if save:
            return self._save_json_output(json.dumps(images, indent=4, sort_keys=True, default=str))

        return images

    def get_audio_to_json(self, save=False):
        manifest = self.content_manifest.get_content()
        audio = main_dict(course_id=self.canvas_course_id,
                           course_title=None,
                           content_type="audio",
                           count=len(manifest),
                           course_url=self.course_page_url
                           )
        count = 0
        for item in manifest:
            if item.is_audio:
                count += 1
                audio['content'].append(audio_item_dict(
                    title=item.title,
                    url=item.url,
                    source_page_url=item.parent.url,
                    source_page_title=item.parent.title,
                    source_page_type=item.parent.__class__.__name__,
                    is_hidden=item.is_hidden,
                    content_type=item.__class__.__name__,
                    mime_type=item.mime_type if item.downloadable is True else None,
                    order=item.order,
                    downloadable=item.downloadable,
                ))
        audio['count'] = count

        if save:
            return self._save_json_output(json.dumps(audio, indent=4, sort_keys=True, default=str))

        return audio

    def all_content_to_json(self, save=True):
        all_content = {
            "total_items": len(self.content_manifest),
            "content": {
                "videos": self.get_videos_to_json(),
                "documents": self.get_documents_to_json(),
                "images": self.get_images_to_json(),
                "audio": self.get_audio_to_json()
            },
            "course_id": self.course_id,
            "scan_date": datetime.datetime.now()

        }

        if save:
            return self._save_json_output(json.dumps(all_content, indent=4, sort_keys=True, default=str))

        return json.dumps(all_content, indent=4, sort_keys=True, default=str)


    def _save_json_output(self, content):

        dirname = os.path.abspath(__file__ + "/../../")
        filename = os.path.join(dirname, f'output\\json\\{self.course_id}.json')

        if os.path.exists(filename):
            os.remove(filename)

        with open(filename, 'w') as f:
            f.write(content)
            f.close()
        return filename


